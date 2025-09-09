"""
This is the main script for this project.
1. Initialize AI models: initializing and establishing client connection for the provided models in the config/settings file.
2.
"""

from config import settings
from Models.Ai import Ai


def initialize_ai_models() -> list[Ai]:
    ai_models: list[Ai] = []
    for model in settings.MODEL_INFO:
        ai_model = Ai(
            settings.MODEL_INFO[model]["name"],
            settings.MODEL_INFO[model]["version"],
            settings.MODEL_INFO[model]["url"],
            settings.MODEL_INFO[model]["key"],
            settings.MODEL_INFO[model]["client_name"]
        )
        ai_models.append(ai_model)
    return ai_models


if __name__ == '__main__':
    ai_models = initialize_ai_models()
