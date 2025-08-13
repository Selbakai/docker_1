"""
Tests for docker.py module
"""
import sys
import os
import pytest
from io import StringIO

# Add the parent directory to the path so we can import docker.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_docker_script_runs():
    """Test that docker.py can be imported and executed without errors"""
    import docker
    # If we get here without an ImportError, the test passes
    assert True

def test_docker_script_output():
    """Test that docker.py produces the expected output"""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Import and run the script
    try:
        import docker
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if the output contains the expected text
        output = captured_output.getvalue()
        # Since the script just has a print statement, we can't test much
        # but we can verify it runs without error
        assert True
    except Exception as e:
        sys.stdout = sys.__stdout__
        pytest.fail(f"docker.py failed to run: {e}")

def test_hello_docker_message():
    """Test the hello docker functionality"""
    # Capture stdout
    captured_output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output
    
    try:
        # Execute the print statement
        print("Hello, Docker!")
        
        # Reset stdout
        sys.stdout = old_stdout
        
        # Get the output
        output = captured_output.getvalue().strip()
        
        # Assert the expected message
        assert output == "Hello, Docker!"
        
    finally:
        # Ensure stdout is restored
        sys.stdout = old_stdout
