""" This file contains the AI functions for the AI module """

import os
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def download_image(image_url: str, save_path: str):
    """
    Download an image from a URL and save it to a path
    """
    response = requests.get(image_url, timeout=5)
    with open(save_path, "wb") as file:
        file.write(response.content)


def generate_image(prompt: str, save_path: str):
    """
    Generate an image with DALL-E
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    download_image(image_url, save_path)
    return f"Link to image: {save_path}"


available_functions = {
    "generate_image": generate_image
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_image",
            "description": "Generate an image from a prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to create the image with"
                    },
                    "save_path": {
                        "type": "string",
                        "description": "The path to save the image to"
                    }
                },
                "required": ["prompt", "save_path"]
            }
        }
    }
]
