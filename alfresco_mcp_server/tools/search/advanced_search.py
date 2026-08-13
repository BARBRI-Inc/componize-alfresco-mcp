"""
Advanced search tool for Alfresco MCP Server.
Each tool is self-contained with its own validation, business logic, and env handling.
"""
import logging
from typing import Optional
from fastmcp import Context

from ...utils.connection import ensure_connection
from ...utils.json_utils import safe_format_output
from ...utils.search_execute import execute_search

logger = logging.getLogger(__name__)


async def advanced_search_impl(
    query: str, 
    sort_field: str = "cm:modified",
    sort_ascending: bool = False,
    max_results: int = 25,
    ctx: Optional[Context] = None
) -> str:
    """Advanced search with sorting and filtering capabilities.
    
    Args:
        query: Search query string (supports Alfresco Full Text Search syntax)
        sort_field: Field to sort by (default: cm:modified)
        sort_ascending: Sort order (default: False for descending)
        max_results: Maximum number of results to return (default: 25)
        ctx: MCP context for progress reporting
    
    Returns:
        Formatted search results with metadata, sorted as requested
    """
    # Parameter validation and extraction
    try:
        # Extract parameters with fallback handling
        if hasattr(query, 'value'):
            actual_query = str(query.value)
        else:
            actual_query = str(query)
            
        if hasattr(sort_field, 'value'):
            actual_sort_field = str(sort_field.value)
        else:
            actual_sort_field = str(sort_field)
            
        if hasattr(sort_ascending, 'value'):
            actual_sort_ascending = bool(sort_ascending.value)
        else:
            actual_sort_ascending = bool(sort_ascending)
            
        if hasattr(max_results, 'value'):
            actual_max_results = int(max_results.value)
        else:
            actual_max_results = int(max_results)
        
        # Clean and normalize for display (preserve Unicode characters)
        safe_query_display = str(actual_query)
        safe_sort_field_display = str(actual_sort_field)
        
    except Exception as e:
        logger.error(f"Parameter extraction error: {e}")
        return f"ERROR: Parameter error: {str(e)}"
    
    if ctx:
        await ctx.info(safe_format_output(f"Advanced search for '{safe_query_display}' with sorting..."))
        await ctx.report_progress(0.0)
    
    try:
        # Get all clients that ensure_connection() already created
        master_client = await ensure_connection()

        from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import (
            RequestPagination,
            RequestQuery,
            RequestQueryLanguage,
            RequestSortDefinitionItem,
            RequestSortDefinitionItemType,
            SearchRequest,
        )

        # Access the search client that was already created
        search_client = master_client.search

        logger.debug(f"Advanced search for: '{safe_query_display}', sort: {safe_sort_field_display} ({'asc' if actual_sort_ascending else 'desc'})")

        if ctx:
            await ctx.report_progress(0.3)

        search_request = SearchRequest(
            query=RequestQuery(query=actual_query, language=RequestQueryLanguage.AFTS),
            paging=RequestPagination(max_items=actual_max_results, skip_count=0),
            sort=[
                RequestSortDefinitionItem(
                    field=actual_sort_field,
                    ascending=actual_sort_ascending,
                    type_=RequestSortDefinitionItemType.FIELD,
                )
            ],
        )

        if ctx:
            await ctx.report_progress(0.5)

        entries, error = execute_search(search_client, search_request)
        if error:
            logger.error(f"Advanced search failed: {error}")
            return safe_format_output(f"ERROR: Advanced search failed - {error}")

        if ctx:
            await ctx.report_progress(1.0)
        
        # Process final results
        if entries:
            logger.info(f"Found {len(entries)} search results")
            result_text = f"Found {len(entries)} item(s) matching '{safe_query_display}':\n\n"
            
            for i, entry in enumerate(entries, 1):
                # Handle different possible entry structures
                node = None
                if isinstance(entry, dict):
                    if 'entry' in entry:
                        node = entry['entry']
                    elif 'name' in entry:  # Direct node structure
                        node = entry
                    else:
                        logger.debug(f"Unknown entry structure: {entry}")
                        continue
                elif hasattr(entry, 'entry'):  # ResultSetRowEntry object
                    node = entry.entry
                else:
                    logger.debug(f"Entry is not a dict or ResultSetRowEntry: {type(entry)}")
                    continue
                
                if node:
                    # Handle both dict and ResultNode objects
                    if isinstance(node, dict):
                        name = str(node.get('name', 'Unknown'))
                        node_id = str(node.get('id', 'Unknown'))
                        node_type_actual = str(node.get('nodeType', 'Unknown'))
                        created_at = str(node.get('createdAt', 'Unknown'))
                    else:
                        # ResultNode object - access attributes directly
                        name = str(getattr(node, 'name', 'Unknown'))
                        node_id = str(getattr(node, 'id', 'Unknown'))
                        node_type_actual = str(getattr(node, 'node_type', 'Unknown'))
                        created_at = str(getattr(node, 'created_at', 'Unknown'))
                    
                    # Apply safe formatting to individual fields to prevent emoji encoding issues
                    safe_name = safe_format_output(name)
                    safe_node_id = safe_format_output(node_id)
                    safe_node_type = safe_format_output(node_type_actual)
                    safe_created_at = safe_format_output(created_at)
                    
                    result_text += f"{i}. {safe_name}\n"
                    result_text += f"   - ID: {safe_node_id}\n"
                    result_text += f"   - Type: {safe_node_type}\n"
                    result_text += f"   - Created: {safe_created_at}\n\n"
            
            return safe_format_output(result_text)
        else:
            # Simple "0" for zero results as requested
            return "0"
        
    except Exception as e:
        error_msg = f"ERROR: Advanced search failed: {str(e)}"
        if ctx:
            await ctx.error(safe_format_output(error_msg))
        return safe_format_output(error_msg) 