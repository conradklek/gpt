""" Beautiful Soup Tools """

import requests
from bs4 import BeautifulSoup


def extract_links(url: str) -> str:
    """
    Extract all hyperlinks from a page
    """
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return str(links)


def extract_text(url: str, selector: str = None) -> str:
    """
    Extract clean text from a page or specific elements
    """
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    if selector:
        elements = soup.select(selector)
        texts = [element.get_text(strip=True) for element in elements]
    else:
        texts = soup.get_text(strip=True)
    return str(texts)


available_functions = {
    "extract_links": extract_links,
    "extract_text": extract_text
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_links",
            "description": "Extract all hyperlinks from a page.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL of the page to parse"
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "extract_text",
            "description": "Extract clean text from a page or specific elements.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL of the page to parse"
                    },
                    "selector": {
                        "type": "string",
                        "description": "The CSS selector to target specific elements (optional)",
                    }
                },
                "required": ["url"]
            }
        }
    }
]
