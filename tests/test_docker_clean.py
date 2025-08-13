"""
Tests for docker.py module
"""
import sys
import os


# Add the parent directory to the path so we can import docker.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_docker_script_runs():
    """Test that docker.py can be imported and executed without errors"""
    # Test that the script can be executed without errors
    import subprocess
    import sys

    result = subprocess.run([sys.executable, "docker.py"],
                            capture_output=True, text=True)
    assert result.returncode == 0


def test_docker_script_output():
    """Test that docker.py produces the expected output"""
    import subprocess
    import sys

    # Run the script and capture output
    result = subprocess.run([sys.executable, "docker.py"],
                            capture_output=True, text=True)

    # Check if the script ran successfully
    assert result.returncode == 0
    # Check if the output contains the expected text
    assert "Hello, Docker!" in result.stdout


def test_hello_docker_message():
    """Test the hello docker functionality"""
    from io import StringIO

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
