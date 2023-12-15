"""
This tool provides a function that sends an HTTP request.
"""

import json
import requests


def make_http_request(url, method, body=None):
    """
    Sends an HTTP request to the specified URL using the given method
    Parameters:
    - url: The URL to which the HTTP request will be sent.
    - method: The HTTP method to use for the request (e.g., GET, POST,PUT, DELETE).
    - body: An optional parameter that contains the request body

    Returns:
    A string representation of the server's response.
    """

    try:
        if body:
            body = json.loads(body)

        response = requests.request(method, url, json=body, timeout=10)

        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)


tools = [
    {
        "type": "function",
        "function": {
            "name": "make_http_request",
            "description": "Sends an HTTP request to the specified URL using the given method.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL to which the HTTP reque will be sent."
                    },
                    "method": {
                        "type": "string",
                        "description": "The HTTP method to use for the request."
                    },
                    "body": {
                        "type": "string",
                        "description": "A string representation of the request body."
                    }
                },
                "required": ["url", "method"]
            }
        }
    }
]
