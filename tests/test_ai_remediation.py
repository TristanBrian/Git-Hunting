import pytest
from app import generate_fix, generate_test, get_download_link

def test_generate_fix_mock_mode():
    security_report = {"score": 60, "findings": [{"name": "AWS Access Key"}]}
    fix = generate_fix("TypeError", "diff", security_report, "auth.py", None, "mock")
    assert "--- a/auth.py" in fix
    assert "+++ b/auth.py" in fix
    assert "os.getenv" in fix

def test_generate_test_mock_mode():
    test_code = generate_test("TypeError", "fix_code", "auth.py", None, "mock")
    assert "def test_auth_regression():" in test_code
    assert "patch" in test_code

def test_get_download_link_formatting():
    content = "hello world"
    link = get_download_link(content, "test.txt", "Download")
    assert "href=\"data:text/plain;base64," in link
    assert "download=\"test.txt\"" in link
    assert "Download" in link
