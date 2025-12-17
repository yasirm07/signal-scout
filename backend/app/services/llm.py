from typing import List

from openai import OpenAI

from app.config import get_settings
from app.schemas import EvidenceItem, Recommendation

settings = get_settings()


def client() -> OpenAI:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is required for LLM synthesis.")
    return OpenAI(api_key=settings.openai_api_key)


def build_recommendations(evidence: List[EvidenceItem]) -> List[Recommendation]:
    """
    Convert evidence into actionable recommendations using the LLM.
    If no API key is provided, return a static sample set.
    """
    if not settings.openai_api_key:
        return [
            Recommendation(
                title="Fix inconsistent opening hours on Google Maps",
                what="Update Google Maps listing to match the website hours.",
                why="Inconsistent hours create customer frustration and lost visits.",
                impact="high",
                evidence=[EvidenceItem(source="google_maps", detail="Maps shows Mon-Fri 9-5"), EvidenceItem(source="website", detail="Site shows Mon-Sat 9-7")],
            ),
            Recommendation(
                title="Add missing service keywords to description",
                what="Clarify top services in the business description.",
                why="Better keywords improve discovery and set expectations.",
                impact="medium",
                evidence=[EvidenceItem(source="website", detail="Homepage lacks service list")],
            ),
        ]

    prompt = f"""
You are generating concise, evidence-backed recommendations for a business presence audit.
Use only the evidence provided. Do not invent facts. Provide 3-5 recommendations.
Return JSON with fields: title, what, why, impact (low/medium/high), evidence (list of short strings).

Evidence:
{[{'source': e.source, 'detail': e.detail} for e in evidence]}
"""
    completion = client().responses.create(
        model=settings.openai_model,
        input=prompt,
        response_format={"type": "json_object"},
    )
    data = completion.output_parsed or {}
    recs = data.get("recommendations") if isinstance(data, dict) else None
    if not recs:
        return []
    results: List[Recommendation] = []
    for rec in recs:
        results.append(
            Recommendation(
                title=rec.get("title", "Recommendation"),
                what=rec.get("what", ""),
                why=rec.get("why", ""),
                impact=rec.get("impact", "medium"),
                evidence=[EvidenceItem(source="llm", detail=item) for item in rec.get("evidence", [])],
            )
        )
    return results

