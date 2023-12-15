"""
HackerNews API Interaction Tool

This tool provides functions to interact with the HackerNews API.
"""
import requests

BASE_URL = 'https://hacker-news.firebaseio.com/v0/'


def get_top_stories(start: int = 0, end: int = 10):
    """
    Retrieves the top stories from HackerNews.
    """
    top_stories = requests.get(f'{BASE_URL}topstories.json?print=pretty')
    top_stories = top_stories.json()[start:end+1]
    output = []
    for story_id in top_stories:
        story = get_item(story_id)
        output.append(story)
    return "\n".join([f"{story['title']}\n{story['url']}" for story in output])


def get_item(item_id):
    """
    Retrieves the details of a specific item by its ID.
    """
    response = requests.get(f'{BASE_URL}item/{item_id}.json?print=pretty')
    return response.json()


available_functions = {
    'get_top_stories': get_top_stories
}

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_top_stories',
            'description': 'Retrieves the top stories from HackerNews.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'start': {
                        'type': 'integer',
                        'description': 'The index of the first story to retrieve.'
                    },
                    'end': {
                        'type': 'integer',
                        'description': 'The index of the last story to retrieve.'
                    }
                },
                'required': ['start', 'end']
            }
        }
    }
]

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        print(get_top_stories(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print('Please provide start and end index as arguments.')
