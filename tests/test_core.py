from issachar.deterministic import qualify
from issachar.outreach import OutreachMessage, OutreachQueue, OutreachStatus
from issachar.schemas import Evidence, Prospect

def prospect():
    return Prospect(
        company="Example Logistics",
        industry="Logistics",
        evidence=[
            Evidence("https://example.com/ops", "Dispatch workflow exists", "2026-10-03"),
            Evidence("https://example.com/jobs", "Operations role coordinates deliveries", "2026-10-03"),
        ],
        workflow=["order", "dispatch", "delivery", "reconciliation"],
        technology_surface=["website", "spreadsheet workflow"],
        buyer_role="Operations Manager",
    )

def test_qualification_gate():
    result = qualify(prospect())
    assert result.qualified is True
    assert result.score == 4

def test_missing_workflow_blocks():
    p = prospect()
    p.workflow = []
    result = qualify(p)
    assert result.qualified is False

def test_outreach_requires_approval():
    q = OutreachQueue()
    m = OutreachMessage("Example", "ops@example.com", "Workflow enquiry", "Hello")
    q.add(m)
    try:
        m.mark_sent()
        assert False
    except ValueError:
        pass
    m.approve()
    m.mark_sent()
    assert m.status == OutreachStatus.SENT
