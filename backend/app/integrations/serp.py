import os
from typing import Any, Dict, List, Tuple

import httpx

from app.config import get_settings

settings = get_settings()


async def search_local_listing(business_name: str, city: str) -> Dict[str, Any]:
    """Query SerpAPI for Google Maps listing candidates.

    If the SERP call fails for any reason (bad key, rate limit, network),
    we fall back to a safe sample result instead of crashing the request.
    """
    fallback = {
        "local_results": [
            {
                "title": f"{business_name} (sample)",
                "address": f"123 Main St, {city}",
                "phone": "(555) 123-4567",
                "hours": "Mon-Fri 9am-5pm",
                "rating": 4.5,
                "reviews": 87,
                "link": "https://maps.google.com/",
            }
        ]
    }

    if not settings.serp_api_key:
        # Offline/demo fallback
        return fallback

    params = {
        "engine": "google_maps",
        "q": f"{business_name} {city}",
        "api_key": settings.serp_api_key,
    }
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            resp = await client.get(settings.serp_base_url, params=params)
            resp.raise_for_status()
            return resp.json()
    except Exception as e:  # best-effort fallback
        print(f"[serp] Falling back to sample data due to error: {e}")
        return fallback


def pick_best_listing(local_results: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], float]:
    """
    Pick the top listing and assign a naive confidence score.
    """
    if not local_results:
        return {}, 0.0
    top = local_results[0]
    confidence = 0.6
    if top.get("rating") and top.get("reviews", 0) > 10:
        confidence += 0.2
    return top, min(confidence, 0.95)

