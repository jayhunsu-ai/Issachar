import pytest
from issachar.policy import ExecutionPolicy

def test_external_send_is_disabled_by_default():
    with pytest.raises(PermissionError):
        ExecutionPolicy().assert_send_allowed(True, 0)

def test_approval_is_required_when_sending_is_enabled():
    policy = ExecutionPolicy(allow_external_send=True)
    with pytest.raises(PermissionError):
        policy.assert_send_allowed(False, 0)
