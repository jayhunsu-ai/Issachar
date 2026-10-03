from dataclasses import dataclass, field
from enum import Enum
from typing import Any

class ProspectStatus(str, Enum):
    DISCOVERED = "DISCOVERED"
    INVESTIGATING = "INVESTIGATING"
    QUALIFIED = "QUALIFIED"
    OUTREACH = "OUTREACH"
    RESPONDED = "RESPONDED"
    CLOSED = "CLOSED"

class EvidenceKind(str, Enum):
    OBSERVATION = "observation"
    INFERENCE = "inference"
    HYPOTHESIS = "hypothesis"

@dataclass(frozen=True)
class Evidence:
    source: str
    observation: str
    collected_at: str
    kind: EvidenceKind = EvidenceKind.OBSERVATION
    confidence: float = 1.0

    def __post_init__(self):
        if not self.source.strip():
            raise ValueError("Evidence source is required")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Evidence confidence must be between 0 and 1")

@dataclass
class Prospect:
    company: str
    industry: str
    website: str | None = None
    location: str | None = None
    company_type: str | None = None
    evidence: list[Evidence] = field(default_factory=list)
    workflow: list[str] = field(default_factory=list)
    technology_surface: list[str] = field(default_factory=list)
    buyer_role: str | None = None
    buyer_contact: str | None = None
    status: ProspectStatus = ProspectStatus.DISCOVERED
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class QualificationResult:
    qualified: bool
    score: int
    reasons: tuple[str, ...]
    blockers: tuple[str, ...]

@dataclass(frozen=True)
class OpportunityHypothesis:
    title: str
    problem: str
    evidence_sources: tuple[str, ...]
    business_impact: str
    capability: str
    confidence: float
    validation_questions: tuple[str, ...]
