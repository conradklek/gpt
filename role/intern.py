""" Role: Intern """

from tool.hackernews_api import (
    available_functions as hackernews_api_functions,
    tools as hackernews_api_tool
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
    "content": "You are a helpful assistant."
}

tools = hackernews_api_tool + file_system_tools + beautiful_soup_tools

available_functions = {
    **hackernews_api_functions,
    **file_system_functions,
    **beautiful_soup_functions
}
