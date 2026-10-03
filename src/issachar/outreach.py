from dataclasses import dataclass
from enum import Enum

class OutreachStatus(str, Enum):
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"
    SENT = "SENT"
    REPLIED = "REPLIED"
    PAUSED = "PAUSED"

@dataclass
class OutreachMessage:
    company: str
    recipient: str
    subject: str
    body: str
    status: OutreachStatus = OutreachStatus.DRAFT
    evidence_source: str | None = None

    def approve(self):
        if self.status != OutreachStatus.DRAFT:
            raise ValueError(f"Cannot approve outreach in state {self.status}")
        self.status = OutreachStatus.APPROVED

    def mark_sent(self):
        if self.status != OutreachStatus.APPROVED:
            raise ValueError("Human approval is required before sending")
        self.status = OutreachStatus.SENT

class OutreachQueue:
    def __init__(self):
        self._items = []

    def add(self, message: OutreachMessage):
        self._items.append(message)

    def pending_approval(self):
        return [x for x in self._items if x.status == OutreachStatus.DRAFT]

    def approved(self):
        return [x for x in self._items if x.status == OutreachStatus.APPROVED]
