from main import get_status_message


def test_get_status_message_returns_expected_message() -> None:
    assert get_status_message() == "Phase 10 GitHub Actions CI project is running"
