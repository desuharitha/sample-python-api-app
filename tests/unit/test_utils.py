import pytest
import json
import os
from tests.utils.excel_report import generate_excel_report

def test_generate_excel_report(tmp_path):
    """Test Excel report generation"""
    # Create sample JSON data
    json_data = {
        "tests": [
            {
                "nodeid": "test_main.py::test_success",
                "outcome": "passed",
                "duration": 0.1
            },
            {
                "nodeid": "test_main.py::test_failure",
                "outcome": "failed",
                "duration": 0.2,
                "call": {
                    "crash": {
                        "message": "AssertionError"
                    }
                }
            }
        ]
    }
    
    json_file = tmp_path / "test_report.json"
    excel_file = tmp_path / "test_report.xlsx"
    
    with open(json_file, 'w') as f:
        json.dump(json_data, f)
    
    generate_excel_report(str(json_file), str(excel_file))
    
    assert excel_file.exists()
    
    # Clean up
    os.remove(json_file)
    os.remove(excel_file)