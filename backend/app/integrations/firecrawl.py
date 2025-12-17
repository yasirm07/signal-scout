import json
from typing import Any, Dict, List

import httpx

from app.config import get_settings

settings = get_settings()


async def crawl_site(url: str) -> Dict[str, Any]:
    """
    Crawl a website using Firecrawl API. Falls back to a stub if no key is set.
    """
    if not url:
        return {"pages": []}

    if not settings.firecrawl_api_key:
        return {
            "pages": [
                {
                    "url": url,
                    "content": "Sample About: We are a family-owned local business offering great service.",
                    "links": [],
                }
            ]
        }

    payload = {"url": url, "maxPages": 3}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.firecrawl_api_key}",
    }
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.post(settings.firecrawl_base_url, headers=headers, content=json.dumps(payload))
        resp.raise_for_status()
        return resp.json()

