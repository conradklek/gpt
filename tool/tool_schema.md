# Tool Schema

When writing tools, follow the schema below. This will help us to maintain a consistent structure for all tools.
IMPORTANT: Do not include any comments in your code. The comments below are only for explanation purposes.

```python
"""
describe the tool.
"""
# Import necessary libraries

# Define global variables or constants

# Define helper functions (if any)

def <tool_function_name>(<parameters>):
    """
    <Function Description>
    """
    # Implement the function logic
    # Return the output AS A STRING

# If there are multiple related functions, define them similarly

# Define the available functions for external use
available_functions = {
    "<tool_function_name>": <tool_function_name>
}

# Define the tool meta information
# Example:
tools = [
    {
        "type": "function",
        "function": {
            "name": "<tool_function_name>",
            "description": "<Function Description>",
            "parameters": {
                "type": "object",
                "properties": {
                    "<Parameter Name>": {
                        "type": "<Parameter Type>",
                        "description": "<Parameter Description>"
                    }
                },
                "required": ["<Parameter Name>"]
            }
        }
    }
]

# Define a CLI with parameters that call the function
# Example:
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(<tool_function_name>(sys.argv[1]))
    else:
        print("No argument provided. Please run the script with an argument.")
```
