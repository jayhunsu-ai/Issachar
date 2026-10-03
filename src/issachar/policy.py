from dataclasses import dataclass

@dataclass(frozen=True)
class ExecutionPolicy:
    allow_external_send: bool = False
    require_human_approval: bool = True
    max_messages_per_run: int = 20
    max_retries: int = 2

    def assert_send_allowed(self, approved: bool, sent_count: int) -> None:
        if not self.allow_external_send:
            raise PermissionError("External sending is disabled by policy")
        if self.require_human_approval and not approved:
            raise PermissionError("Human approval is required")
        if sent_count >= self.max_messages_per_run:
            raise PermissionError("Per-run send limit reached")
