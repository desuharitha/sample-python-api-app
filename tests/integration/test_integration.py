import subprocess
import sys
import pytest

def test_main_script_execution():
    """Integration test: Run main.py and check output"""
    # Run the main.py script
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="."
    )
    
    # Check exit code
    assert result.returncode == 0
    
    # Check output contains expected text
    output = result.stdout
    assert "Fetched data from API:" in output
    assert "Title:" in output
    assert "Body:" in output