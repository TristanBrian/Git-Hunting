import pytest
from app import run_security_scan

def test_aws_access_key_detection():
    diff_text = """
+ AWS_KEY = "AKIA1234567890ABCDEF"
    """
    report = run_security_scan(diff_text)
    assert report["score"] == 85
    assert len(report["findings"]) == 1
    assert report["findings"][0]["name"] == "AWS Access Key"
    assert report["findings"][0]["severity"] == "Critical"

def test_stripe_live_key_detection():
    diff_text = '+ STRIPE_SECRET = "mock_stripe_key_123456789012345678901234"'
    report = run_security_scan(diff_text)
    assert report["score"] == 55
    assert report["findings"][0]["name"] == "Stripe Live"

def test_sql_injection_detection():
    diff_text = """
+ query = "SELECT * FROM users WHERE id = '" + user_input + "'"
+ cursor.execute(query)
    """
    report = run_security_scan(diff_text)
    assert report["score"] == 80
    assert report["findings"][0]["type"] == "SQL Injection"

def test_jwt_token_detection():
    diff_text = """
+ TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    """
    report = run_security_scan(diff_text)
    assert report["score"] == 70
    assert report["findings"][0]["name"] == "JWT Token hardcoded"

def test_clean_diff_score():
    diff_text = """
+ def add(a, b):
+     return a + b
    """
    report = run_security_scan(diff_text)
    assert report["score"] == 100
    assert len(report["findings"]) == 0
