import pytest
from unittest.mock import patch, MagicMock
import main

@patch('main.requests.get')
def test_main_success(mock_get):
    """Test main function with successful API response"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'title': 'Test Title',
        'body': 'Test Body'
    }
    mock_get.return_value = mock_response
    
    # Capture print output
    with patch('builtins.print') as mock_print:
        main.main()
        
        # Check prints
        mock_print.assert_any_call("Fetched data from API:")
        mock_print.assert_any_call("Title: Test Title")
        mock_print.assert_any_call("Body: Test Body")

@patch('main.requests.get')
def test_main_failure(mock_get):
    """Test main function with failed API response"""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    with patch('builtins.print') as mock_print:
        main.main()
        
        mock_print.assert_called_with("Failed to fetch data. Status code: 404")

@patch('main.requests.get')
def test_main_exception(mock_get):
    """Test main function with request exception"""
    mock_get.side_effect = Exception("Network error")
    
    with patch('builtins.print') as mock_print:
        with pytest.raises(Exception):
            main.main()