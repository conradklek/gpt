""" Role: Designer """

from tool.describe_image import (
    available_functions as describe_image_functions,
    tools as describe_image_tool
)
from tool.generate_image import (
    available_functions as generate_image_functions,
    tools as generate_image_tool
)

system = {
    "role": "system",
    "content": "You are a brilliant designer capable of describing and creating images."
}

tools = describe_image_tool + generate_image_tool

available_functions = {
    **describe_image_functions,
    **generate_image_functions
}
