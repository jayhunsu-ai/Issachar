from dataclasses import dataclass
from typing import Protocol, Sequence
from .schemas import Evidence, Prospect

class ModelAdapter(Protocol):
    def generate(self, *, system: str, prompt: str) -> str: ...

@dataclass(frozen=True)
class ModelRequest:
    system: str
    prompt: str

class NullModel:
    def generate(self, *, system: str, prompt: str) -> str:
        raise RuntimeError("No model adapter configured")

def build_opportunity_prompt(prospect: Prospect, evidence: Sequence[Evidence]) -> ModelRequest:
    evidence_text = "\n".join(
        f"- {item.observation} [source: {item.source}]" for item in evidence
    )
    return ModelRequest(
        system=(
            "You are Issachar's bounded analysis model. Separate observations "
            "from inferences and hypotheses. Never invent evidence or contacts."
        ),
        prompt=(
            f"Company: {prospect.company}\nIndustry: {prospect.industry}\n"
            f"Evidence:\n{evidence_text}\n"
            "Produce only evidence-grounded opportunity hypotheses and validation questions."
        ),
    )
