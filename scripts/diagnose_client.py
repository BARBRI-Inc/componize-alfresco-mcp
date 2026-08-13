#!/usr/bin/env python3
"""
Reproduces the exact code paths advanced_search_impl / cmis_search_impl use
(via python-alfresco-api's real client + models), printing the exact request
body sent and the exact raw response, to see where the parsing breaks down.

Usage:
    uv run python scripts/diagnose_client.py

Reads ALFRESCO_URL / ALFRESCO_USERNAME / ALFRESCO_PASSWORD from the
environment; prompts for anything missing (password entry is hidden).
"""
import getpass
import os

from python_alfresco_api import ClientFactory
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.models import (
    RequestPagination,
    RequestQuery,
    RequestQueryLanguage,
    RequestSortDefinitionItem,
    RequestSortDefinitionItemType,
    SearchRequest,
)
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.types import UNSET
from python_alfresco_api.raw_clients.alfresco_search_client.search_client.api.search.search import (
    sync_detailed as raw_search_sync_detailed,
)

BASE = (os.environ.get("ALFRESCO_URL") or input("ALFRESCO_URL (bare host): ").strip()).rstrip("/")
USER = os.environ.get("ALFRESCO_USERNAME") or input("Username: ").strip()
PASSWORD = os.environ.get("ALFRESCO_PASSWORD") or getpass.getpass("Password: ")


def run_case(label, search_request):
    print(f"\n=== {label} ===")
    print("Request body sent:", search_request.to_dict())

    factory = ClientFactory(base_url=BASE, username=USER, password=PASSWORD, verify_ssl=True, timeout=30)
    search_client = factory.create_search_client()
    raw_client = search_client.search.raw_client

    resp = raw_search_sync_detailed(client=raw_client, body=search_request)
    print("HTTP status:", resp.status_code)
    print("parsed is None:", resp.parsed is None)
    if resp.parsed is None:
        print("raw content (first 800 chars):", resp.content[:800])
    else:
        print("parsed.list_:", resp.parsed.list_)
        if resp.parsed.list_ and resp.parsed.list_ != UNSET:
            print("entries count:", len(resp.parsed.list_.entries))


def main():
    # Mirrors advanced_search_impl's default call: query + default sort_field="cm:modified"
    sorted_request = SearchRequest(
        query=RequestQuery(query="TEXT:test", language=RequestQueryLanguage.AFTS),
        paging=RequestPagination(max_items=5, skip_count=0),
        sort=[
            RequestSortDefinitionItem(
                field="cm:modified",
                ascending=False,
                type_=RequestSortDefinitionItemType.FIELD,
            )
        ],
    )
    run_case("advanced_search-style (AFTS + sort=cm:modified)", sorted_request)

    unsorted_request = SearchRequest(
        query=RequestQuery(query="TEXT:test", language=RequestQueryLanguage.AFTS),
        paging=RequestPagination(max_items=5, skip_count=0),
    )
    run_case("plain AFTS (no sort)", unsorted_request)

    cmis_request = SearchRequest(
        query=RequestQuery(query="SELECT * FROM cmis:document", language=RequestQueryLanguage.CMIS),
        paging=RequestPagination(max_items=5, skip_count=0),
        include=UNSET,
    )
    run_case("cmis_search-style", cmis_request)


if __name__ == "__main__":
    main()
