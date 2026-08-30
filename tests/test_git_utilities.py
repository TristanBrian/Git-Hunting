import os
import tempfile
import pytest
from app import get_git_diff, cleanup_repo

def test_git_diff_fallback_generic_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a dummy file in temp_dir
        with open(os.path.join(temp_dir, "test.py"), "w") as f:
            f.write("print('hello world')")
        
        target_file, diff = get_git_diff(temp_dir, "generic build error check envs")
        assert target_file == "Overall Repository"
        assert "No recent commits found." in diff or "git" in diff

def test_git_diff_file_extraction():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.makedirs(os.path.join(temp_dir, "src"), exist_ok=True)
        file_path = os.path.join(temp_dir, "src", "auth.py")
        with open(file_path, "w") as f:
            f.write("def get_user(): pass")

        error_log = "File 'src/auth.py', line 10, in get_user\nTypeError: error"
        target_file, diff = get_git_diff(temp_dir, error_log)
        assert target_file == "src/auth.py"
        assert "File content" in diff or "git" in diff

def test_cleanup_repo_safe():
    temp_dir = tempfile.mkdtemp(prefix="ghost_test_")
    assert os.path.exists(temp_dir)
    cleanup_repo(temp_dir)
    assert not os.path.exists(temp_dir)
