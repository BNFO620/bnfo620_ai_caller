import os
from dotenv import load_dotenv
load_dotenv()


# each models information, the main function will create an instance of the model and establish the connection
MODEL_INFO = {
    "CHATGPT": {
        "name": "CHATGPT",
        "version": "gpt-4o-mini",
        "url": None,  # OpenAI default
        "key": os.getenv("CHATGPT_KEY"),
        "client_name": "OPENAI"
    },
    "GEMINI": {
        "name": "GEMINI",
        "version": "gemini-2.5-flash",
        "url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "key": os.getenv("GEMINI_KEY"),
        "client_name": "OPENAI"
    },
    "DEEPSEEK": {
        "name": "DEEPSEEK",
        "version": "deepseek-chat",
        "url": "https://api.deepseek.com/v1",
        "key": os.getenv("DEEPSEEK_KEY"),
        "client_name": "OPENAI"
    },
    "CLAUDE": {
        "name": "CLAUDE",
        "version": "claude-3.5-sonnet",
        "url": None,  # Anthropic default
        "key": os.getenv("CLAUDE_KEY"),
        "client_name": "ANTHROPIC"
    }
}
