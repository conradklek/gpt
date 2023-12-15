""" ChatGPT Subprocess Tools """

import subprocess


def execute_subprocess(command: str) -> str:
    """
    Run a terminal command and return the output.
    """
    result = subprocess.run(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            text=True,
                            check=True
                            )
    return result.stdout


available_functions = {
    "execute_subprocess": execute_subprocess
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "execute_subprocess",
            "description": "Run subprocesses or terminal commands",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to execute"
                    }
                },
                "required": ["command"]
            }
        }
    }
]
