""" ChatGPT File System Tools """

import os


def write_file(path: str, content: str) -> str:
    """
    Save a text file to a path
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return f"Saved to {path}"


def read_file(path: str) -> str:
    """
    Read a text file from a path
    """
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def list_directory(path: str) -> str:
    """
    List all the files in a directory
    """
    files = os.listdir(path)
    return "\n".join(files)


def delete_file(path: str) -> str:
    """
    Delete a file
    """
    os.remove(path)
    return f"Deleted {path}"


def delete_directory(path: str) -> str:
    """
    Delete a directory
    """
    os.rmdir(path)
    return f"Deleted {path}"


def create_directory(path: str) -> str:
    """
    Crete a directory
    """
    os.mkdir(path)
    return f"Created {path}"


def file_system_command(command: str, path: str, content: str = None) -> str:
    """
    Interact with the file system
    """
    commands = {
        "write_file": write_file,
        "read_file": read_file,
        "list_directory": list_directory,
        "delete_file": delete_file,
        "delete_directory": delete_directory,
        "create_directory": create_directory
    }

    if command in commands:
        if content:
            return commands[command](path, content)
        return commands[command](path)
    return "Invalid command"


available_functions = {
    "file_system_command": file_system_command
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "file_system_command",
            "description": "Interact with the file system",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to use",
                        "enum": [
                            "write_file",
                            "read_file",
                            "list_directory",
                            "delete_file",
                            "delete_directory",
                            "create_directory"
                        ]
                    },
                    "path": {
                        "type": "string",
                        "description": "The path to write the text to"
                    },
                    "content": {
                        "type": "string",
                        "description": "The text content to write to the file"
                    }
                },
                "required": ["command", "path"]
            }
        }
    }
]
