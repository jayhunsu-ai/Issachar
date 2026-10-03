import json
from pathlib import Path
from email.message import EmailMessage
from .outreach import OutreachMessage

REQUIRED_FIELDS = ("company", "recipient", "subject", "body")

def load_campaign(path: str | Path) -> list[OutreachMessage]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    messages = []
    for record in data["records"]:
        missing = [key for key in REQUIRED_FIELDS if not record.get(key)]
        if missing:
            raise ValueError(f"{record.get('company', '<unknown>')}: missing {', '.join(missing)}")
        messages.append(OutreachMessage(
            company=record["company"],
            recipient=record["recipient"],
            subject=record["subject"],
            body=record["body"],
        ))
    return messages

def validate_campaign(path: str | Path) -> tuple[bool, list[str]]:
    errors = []
    try:
        messages = load_campaign(path)
    except (OSError, json.JSONDecodeError, KeyError, ValueError) as exc:
        return False, [str(exc)]
    seen = set()
    for message in messages:
        key = (message.company.lower(), message.recipient.lower(), message.subject.lower())
        if key in seen:
            errors.append(f"duplicate: {message.company} / {message.recipient}")
        seen.add(key)
    return not errors, errors

def render_eml(message: OutreachMessage) -> str:
    msg = EmailMessage()
    msg["To"] = message.recipient
    msg["Subject"] = message.subject
    msg["X-Issachar-Status"] = message.status.value
    msg.set_content(message.body)
    return msg.as_string()
