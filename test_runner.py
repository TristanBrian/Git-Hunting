import unittest
import os
import tempfile
from app import run_security_scan, get_git_diff, cleanup_repo, generate_fix, generate_test, get_download_link

class TestGhostSentinel(unittest.TestCase):

    def test_aws_access_key_detection(self):
        diff_text = '+ AWS_KEY = "AKIA1234567890ABCDEF"'
        report = run_security_scan(diff_text)
        self.assertEqual(report["score"], 85)
        self.assertEqual(len(report["findings"]), 1)
        self.assertEqual(report["findings"][0]["name"], "AWS Access Key")

    def test_stripe_live_key_detection(self):
        diff_text = '+ STRIPE_SECRET = "mock_stripe_key_123456789012345678901234"'
        report = run_security_scan(diff_text)
        self.assertEqual(report["score"], 85)
        self.assertEqual(report["findings"][0]["name"], "Stripe Live")

    def test_sql_injection_detection(self):
        diff_text = "+ query = \"SELECT * FROM users WHERE id = '\" + user_input + \"'\""
        report = run_security_scan(diff_text)
        self.assertEqual(report["score"], 80)
        self.assertEqual(report["findings"][0]["type"], "SQL Injection")

    def test_jwt_token_detection(self):
        diff_text = '+ TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"'
        report = run_security_scan(diff_text)
        self.assertEqual(report["score"], 85)

    def test_clean_diff_score(self):
        diff_text = "+ def add(a, b):\n+     return a + b"
        report = run_security_scan(diff_text)
        self.assertEqual(report["score"], 100)
        self.assertEqual(len(report["findings"]), 0)

    def test_git_diff_fallback(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target_file, diff = get_git_diff(temp_dir, "check for envs error")
            self.assertEqual(target_file, "Overall Repository (last commit)")

    def test_cleanup_repo(self):
        temp_dir = tempfile.mkdtemp(prefix="ghost_test_")
        self.assertTrue(os.path.exists(temp_dir))
        cleanup_repo(temp_dir)
        self.assertFalse(os.path.exists(temp_dir))

    def test_generate_fix_mock(self):
        report = {"score": 60, "findings": [{"name": "AWS Access Key"}]}
        fix = generate_fix("TypeError", "diff", report, "auth.py", None, "mock")
        self.assertIn("--- a/auth.py", fix)
        self.assertIn("os.getenv", fix)

    def test_generate_test_mock(self):
        test_code = generate_test("TypeError", "fix", "auth.py", None, "mock")
        self.assertIn("def test_auth_regression():", test_code)

    def test_download_link(self):
        link = get_download_link("data", "patch.diff", "Download Patch")
        self.assertIn('download="patch.diff"', link)

if __name__ == "__main__":
    unittest.main()
