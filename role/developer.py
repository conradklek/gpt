""" Role: Developer """

from tool.execute_subprocess import (
    available_functions as execute_subprocess_functions,
    tools as subprocess_tool
)
from tool.file_system_command import (
    available_functions as file_system_functions,
    tools as file_system_tools
)
from tool.beautiful_soup import (
    available_functions as beautiful_soup_functions,
    tools as beautiful_soup_tools
)

system = {
    "role": "system",
    "content": """\
You are a supercomputer. \
Break down complex problems into smaller ones. \
Take a deep breath. Now focus on the task at hand."""
}

tools = subprocess_tool + file_system_tools + beautiful_soup_tools

available_functions = {
    **execute_subprocess_functions,
    **file_system_functions,
    **beautiful_soup_functions
}
