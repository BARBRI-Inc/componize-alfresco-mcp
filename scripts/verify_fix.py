#!/usr/bin/env python3
"""
Calls the actual MCP tool implementations (search_content_impl, advanced_search_impl,
cmis_search_impl, search_by_metadata_impl, browse_repository_impl) directly, exactly
as fastmcp_server.py wires them up -- to verify the search_execute.py fix works
end-to-end through the real tool code, not just the raw client.

Usage:
    uv run python scripts/verify_fix.py
"""
import asyncio
import getpass
import os

os.environ.setdefault("ALFRESCO_URL", os.environ.get("ALFRESCO_URL") or input("ALFRESCO_URL (bare host): ").strip())
os.environ.setdefault("ALFRESCO_USERNAME", os.environ.get("ALFRESCO_USERNAME") or input("Username: ").strip())
os.environ.setdefault("ALFRESCO_PASSWORD", os.environ.get("ALFRESCO_PASSWORD") or getpass.getpass("Password: "))
os.environ.setdefault("ALFRESCO_AUTH_METHOD", "basic")

from alfresco_mcp_server.tools.search.search_content import search_content_impl
from alfresco_mcp_server.tools.search.advanced_search import advanced_search_impl
from alfresco_mcp_server.tools.search.cmis_search import cmis_search_impl
from alfresco_mcp_server.tools.search.search_by_metadata import search_by_metadata_impl
from alfresco_mcp_server.tools.core.browse_repository import browse_repository_impl


def show(label, result):
    print(f"\n=== {label} ===")
    print(result[:500])


async def main():
    show("search_content_impl('test', max_results=3)", await search_content_impl("test", max_results=3))
    show(
        "advanced_search_impl('TEXT:test', max_results=3)",
        await advanced_search_impl("TEXT:test", max_results=3),
    )
    show(
        "cmis_search_impl(SELECT * FROM cmis:document, max_results=3)",
        await cmis_search_impl("SELECT * FROM cmis:document", max_results=3),
    )
    show(
        "search_by_metadata_impl(term='test', max_results=3)",
        await search_by_metadata_impl(term="test", max_results=3),
    )
    show("browse_repository_impl('-root-')", await browse_repository_impl("-root-"))


if __name__ == "__main__":
    asyncio.run(main())
