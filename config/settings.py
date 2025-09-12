import os
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
from dotenv import load_dotenv
from google import genai

load_dotenv()

# set the input and output file paths
INPUT_FILE_PATH = "data/reference_data/test_data.csv"
OUTPUT_FILE_PATH = "data/program_data/program_data.csv"

# set each models information
AI_MODELS = {
    "CHATGPT": {
        "version": "gpt-4o-mini",
        "client": AsyncOpenAI(api_key=os.getenv("CHATGPT_KEY")),
    },
    "GEMINI": {
        "version": "gemini-2.5-flash",
        "client": genai.client.Client(api_key=os.getenv("GEMINI_KEY")),
    },
    "DEEPSEEK": {
        "version": "deepseek-chat",
        "client": AsyncOpenAI(api_key=os.getenv("DEEPSEEK_KEY"), base_url="https://api.deepseek.com/v1/"),
    },
    "CLAUDE": {
        "version": "claude-sonnet-4-20250514",
        "client": AsyncAnthropic(api_key=os.getenv("CLAUDE_KEY")),
    }
}

# schema
SCHEMA = {
    "Organism": {
        "genus": "str",
        "species": "str",
        "traits": {
            "column_id": "str",
            "name": "str",
            "units": "str | None",
            "value_format": "str",
            "values": {
                "reference_value": "str",
                "ai_response": {
                    "model": "str",
                    "value": "str"
                }
            }
        }
    }
}

