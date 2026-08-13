"""
Direct search execution against python-alfresco-api's search client.

Bypasses python_alfresco_api.utils.search_utils entirely: search_utils.advanced_search()
calls `search_client.search(body=...)` where `search_client.search` is itself a property
(not the callable it's treated as), which raises TypeError on every call and is silently
swallowed by an internal fallback. That fallback can leak the raw, unparsed Response
wrapper past callers expecting a parsed model, which is what produced the "unknown
SearchResult structure" / "invalid response from Alfresco" errors seen against a real,
working Componize/Alfresco instance -- confirmed by calling search.search_detailed()
directly (the pattern below) and getting correct results for the same queries.
"""
import logging
from typing import Any, List, Optional, Tuple

logger = logging.getLogger(__name__)


def execute_search(search_client, search_request) -> Tuple[Optional[List[Any]], Optional[str]]:
    """Run a SearchRequest against Alfresco. Returns (entries, error).

    On success, entries is a list (possibly empty for a clean zero-result search) and
    error is None. On failure, entries is None and error describes what actually went
    wrong, including Alfresco's real HTTP status and response body where available.
    """
    try:
        resp = search_client.search.search_detailed(search_request)
    except Exception as e:
        return None, f"Search request failed: {e}"

    if resp.parsed is None:
        body = resp.content.decode("utf-8", errors="replace") if resp.content else ""
        return None, f"Alfresco returned HTTP {resp.status_code}: {body[:500]}"

    list_ = resp.parsed.list_
    if not list_:
        # A well-formed response can legitimately omit `list` only when something upstream
        # (proxy, unexpected body shape) failed silently -- treat as empty, not an error.
        return [], None

    return list(list_.entries) if list_.entries else [], None
