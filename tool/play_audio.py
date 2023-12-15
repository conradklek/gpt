"""Play audio from a file"""
import sys
from pydub import AudioSegment
from pydub.playback import play


def play_audio(path: str) -> str:
    """
    Plays audio from a file.
    """
    play(AudioSegment.from_mp3(path))
    return "Audio played successfully."


available_functions = {
    "play_audio": play_audio
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "play_audio",
            "description": "Plays audio from a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "The path to the audio file."
                    }
                },
                "required": ["path"]
            }
        }
    }
]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(play_audio(sys.argv[1]))
    else:
        print("No path provided.")
