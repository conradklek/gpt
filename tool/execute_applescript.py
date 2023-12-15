""" ChatGPT AppleScript Tools """

import subprocess


def execute_applescript(script: str) -> str:
    """
    Run an AppleScript and return the output.
    """
    # The osascript command is used to run AppleScript from the command line in macOS
    result = subprocess.run(['osascript', '-e', script],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            check=True
                            )
    return f'Output:\n{result.stdout}\nError:\n{result.stderr}\nExit Code: {result.returncode}'


available_functions = {
    "execute_applescript": execute_applescript
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "execute_applescript",
            "description": "Run an AppleScript command",
            "parameters": {
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": "The AppleScript code to execute"
                    }
                },
                "required": ["script"]
            }
        }
    }
]
