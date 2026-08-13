#!/usr/bin/env python3
"""
Standalone diagnostic against a real Componize/Alfresco instance, bypassing
python-alfresco-api's model layer entirely so we see the server's raw
status code and response body for each call.

Usage:
    uv run python scripts/diagnose_live.py

Reads ALFRESCO_URL / ALFRESCO_USERNAME / ALFRESCO_PASSWORD from the
environment; prompts for anything missing (password entry is hidden).
Prints only status codes and response bodies -- never echoes the password.
"""
import getpass
import json
import os

import httpx

BASE = os.environ.get("ALFRESCO_URL") or input("ALFRESCO_URL (bare host, e.g. https://barbri.componize.com): ").strip()
BASE = BASE.rstrip("/")
USER = os.environ.get("ALFRESCO_USERNAME") or input("Username: ").strip()
PASSWORD = os.environ.get("ALFRESCO_PASSWORD") or getpass.getpass("Password: ")

AUTH = (USER, PASSWORD)


def show(label, resp):
    print(f"\n=== {label} ===")
    print(f"status: {resp.status_code}")
    body = resp.text
    print(f"body (first 800 chars):\n{body[:800]}")


def main():
    with httpx.Client(auth=AUTH, verify=True, timeout=30) as client:
        # 1. Sanity: who am I
        r = client.get(f"{BASE}/alfresco/api/-default-/public/alfresco/versions/1/people/-me-")
        show("whoami", r)

        # 2. Browse: the exact call browse_repository makes by default (-my-)
        r = client.get(f"{BASE}/alfresco/api/-default-/public/alfresco/versions/1/nodes/-my-/children")
        show("browse nodes/-my-/children", r)

        r = client.get(f"{BASE}/alfresco/api/-default-/public/alfresco/versions/1/nodes/-root-/children")
        show("browse nodes/-root-/children", r)

        # 3. AFTS search (what advanced_search/search_content use)
        afts_body = {"query": {"query": "TEXT:test", "language": "afts"}, "paging": {"maxItems": 5}}
        r = client.post(
            f"{BASE}/alfresco/api/-default-/public/search/versions/1/search",
            json=afts_body,
        )
        show("AFTS search", r)

        # 4. CMIS search (what cmis_search uses)
        cmis_body = {
            "query": {"query": "SELECT * FROM cmis:document", "language": "cmis"},
            "paging": {"maxItems": 5},
        }
        r = client.post(
            f"{BASE}/alfresco/api/-default-/public/search/versions/1/search",
            json=cmis_body,
        )
        show("CMIS search", r)


if __name__ == "__main__":
    main()
