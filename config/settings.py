import os
import openai
import anthropic
from dotenv import load_dotenv
from google import genai

load_dotenv()


# set each models information
AI_MODELS = {
    "CHATGPT": {
        "version": "gpt-4o-mini",
        "max_tokens": 500,
        "temperature": 0,
        "client": openai.OpenAI(api_key=os.getenv("CHATGPT_KEY")),
    },
    "GEMINI": {
        "version": "gemini-2.5-flash",
        "max_tokens": 500,
        "temperature": 0,
        "client": genai.client.Client(api_key=os.getenv("GEMINI_KEY")),
    },
    "DEEPSEEK": {
        "version": "deepseek-chat",
        "max_tokens": 500,
        "temperature": 0,
        "client": openai.OpenAI(api_key=os.getenv("DEEPSEEK_KEY"), base_url="https://api.deepseek.com/v1/"),
    },
    "CLAUDE": {
        "version": "claude-sonnet-4-20250514",
        "max_tokens": 500,
        "temperature": 0,
        "client": anthropic.Anthropic(api_key=os.getenv("CLAUDE_KEY")),
    }
}


# set the input and output file paths
INPUT_FILE_PATH = "data/reference_data/test_data.csv"
OUTPUT_FILE_PATH = "data/program_data/test_program_data.csv"
