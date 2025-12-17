from typing import Dict, List

from app.integrations.serp import pick_best_listing, search_local_listing
from app.integrations.firecrawl import crawl_site
from app.schemas import (
    AnalysisResult,
    EvidenceItem,
    Listing,
    Recommendation,
    SubScores,
)
from app.services.llm import build_recommendations


async def run_analysis(business_name: str, city: str, website: str | None) -> AnalysisResult:
    progress: List[str] = []

    # 1) Discovery
    progress.append("Searching for your business on Maps...")
    serp_data = await search_local_listing(business_name, city)
    listing_raw, confidence = pick_best_listing(serp_data.get("local_results", []))

    listing = Listing(
        name=listing_raw.get("title", business_name),
        address=listing_raw.get("address"),
        phone=listing_raw.get("phone"),
        hours=listing_raw.get("hours"),
        rating=listing_raw.get("rating"),
        review_count=listing_raw.get("reviews"),
        url=listing_raw.get("link"),
        confidence=confidence,
    )

    # 2) Crawl site
    progress.append("Crawling your website for signals...")
    crawl = await crawl_site(website) if website else {"pages": []}

    # 3) Build evidence
    evidence: List[EvidenceItem] = []
    if listing.address:
        evidence.append(EvidenceItem(source="google_maps", detail=f"Address: {listing.address}"))
    if listing.hours:
        evidence.append(EvidenceItem(source="google_maps", detail=f"Hours: {listing.hours}"))
    if listing.phone:
        evidence.append(EvidenceItem(source="google_maps", detail=f"Phone: {listing.phone}"))

    for page in crawl.get("pages", [])[:2]:
        content = page.get("content", "")
        if content:
            snippet = content[:320]
            evidence.append(EvidenceItem(source="website", detail=snippet))

    # 4) Heuristic scores
    sub_scores = SubScores(
        listings_accuracy=int(confidence * 100),
        reputation=70 if listing.review_count else 50,
        online_presence=70 if website else 50,
        trust_signals=65,
    )
    total = int(
        (sub_scores.listings_accuracy * 0.35)
        + (sub_scores.reputation * 0.25)
        + (sub_scores.online_presence * 0.25)
        + (sub_scores.trust_signals * 0.15)
    )

    # 5) Recommendations
    progress.append("Generating recommendations...")
    top_fixes: List[Recommendation] = build_recommendations(evidence)

    return AnalysisResult(
        business_health_score=total,
        sub_scores=sub_scores,
        listing=listing,
        top_fixes=top_fixes,
        evidence=evidence,
        progress=progress,
    )

