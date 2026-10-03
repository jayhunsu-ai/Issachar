from .schemas import Prospect, QualificationResult

def qualify(prospect: Prospect) -> QualificationResult:
    reasons = []
    blockers = []
    score = 0
    if len(prospect.evidence) >= 2:
        score += 1
        reasons.append("sufficient evidence density")
    else:
        blockers.append("insufficient evidence density")
    if prospect.workflow:
        score += 1
        reasons.append("observable workflow recorded")
    else:
        blockers.append("no observable workflow")
    if prospect.technology_surface:
        score += 1
        reasons.append("technology surface recorded")
    else:
        blockers.append("no technology/system surface recorded")
    if prospect.buyer_role or prospect.buyer_contact:
        score += 1
        reasons.append("conversation path identified")
    else:
        blockers.append("no conversation path identified")
    return QualificationResult(score == 4 and not blockers, score, tuple(reasons), tuple(blockers))
