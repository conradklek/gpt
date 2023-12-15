""" Executes a Python script from a string and returns the output. """

import subprocess


def execute_python_script(script_content):
    """
    Executes a Python script passed in as a string and returns the output.
    Parameters:
    - script_content (str): The Python script to execute.
    Returns:
    - output (str): The stdout and stderr of the executed script.
    """
    try:
        result = subprocess.run(
            ['python', '-c', script_content],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout + result.stderr
    except subprocess.CalledProcessError as e:
        return e.output


available_functions = {
    "execute_python_script": execute_python_script
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "execute_python_script",
            "description": "Executes a Python script from a string and returns the output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "script_content": {
                        "type": "string",
                        "description": "The Python script to execute."
                    }
                },
                "required": ["script_content"]
            }
        }
    }
]
