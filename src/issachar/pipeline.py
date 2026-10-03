from dataclasses import dataclass
from .deterministic import qualify
from .model import ModelAdapter, build_opportunity_prompt
from .schemas import Prospect, ProspectStatus

@dataclass
class PipelineResult:
    prospect: Prospect
    qualification: object
    model_output: str | None = None

class IntelligencePipeline:
    def __init__(self, model: ModelAdapter | None = None):
        self.model = model

    def run(self, prospect: Prospect) -> PipelineResult:
        qualification = qualify(prospect)
        if not qualification.qualified:
            return PipelineResult(prospect, qualification)
        prospect.status = ProspectStatus.QUALIFIED
        if self.model is None:
            return PipelineResult(prospect, qualification)
        request = build_opportunity_prompt(prospect, prospect.evidence)
        output = self.model.generate(system=request.system, prompt=request.prompt)
        return PipelineResult(prospect, qualification, output)
