# Outreach Automation

The outreach subsystem prepares and queues prospect emails while keeping external communication human-gated.

## Flow
prospect -> evidence -> outreach hypothesis -> draft -> human approval -> send adapter -> delivery event -> reply/outcome

## Rules
1. Draft generation may be automated.
2. Draft creation never means sent.
3. Only APPROVED messages may reach a transport adapter.
4. Every send creates an audit event.
5. Provider failures cannot retry indefinitely.
6. Rate limits and suppression lists belong to deterministic transport.
7. Replies update state; they do not automatically trigger another send.

## Provider design
Use an adapter interface for Gmail, SMTP or transactional email. Credentials and provider secrets never belong in the repository.
