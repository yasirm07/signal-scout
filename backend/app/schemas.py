from typing import List, Optional
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    business_name: str = Field(..., description="Business name")
    city: str = Field(..., description="City or location")
    website: Optional[str] = Field(None, description="Official website URL, optional")


class Listing(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    hours: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    url: Optional[str] = None
    confidence: float = 0.0


class EvidenceItem(BaseModel):
    source: str
    detail: str


class Recommendation(BaseModel):
    title: str
    what: str
    why: str
    impact: str
    evidence: List[EvidenceItem]


class SubScores(BaseModel):
    listings_accuracy: int
    reputation: int
    online_presence: int
    trust_signals: int


class AnalysisResult(BaseModel):
    business_health_score: int
    sub_scores: SubScores
    listing: Listing
    top_fixes: List[Recommendation]
    evidence: List[EvidenceItem]
    progress: List[str]

