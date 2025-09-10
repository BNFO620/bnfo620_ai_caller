"""
Makes a request to each AI model and returns the response
"""
from config import settings


def fetch_ai_responses(prompt):
    print(f"fetching response for prompt: {prompt}")
    responses: dict[str, str] = {}

    for model_name, model_configuration in settings.AI_MODELS.items():
        model = model_name
        version = model_configuration["version"]
        max_tokens = model_configuration["max_tokens"]
        temperature = model_configuration["temperature"]
        client = model_configuration["client"]
        messages = [{"role": "user", "content": prompt}]

        # fetch claude response
        if model == "CLAUDE":
            raw_response = client.messages.create(
                model=version,
                max_tokens=max_tokens,
                messages=messages
            )
            responses[model] = raw_response.content[0].text.strip()

        # fetch gemini response
        elif model == "GEMINI":
            raw_response = client.models.generate_content(
                model=version,
                contents=prompt
            )
            responses[model] = raw_response.text

        # fetch deepseek response
        elif model == "DEEPSEEK":
            raw_response = client.chat.completions.create(
                model=version,
                temperature=temperature,
                messages=messages
            )
            responses[model] = raw_response.choices[0].message.content

        # fetch chatgpt response
        elif model == "CHATGPT":
            raw_response = client.chat.completions.create(
                model=version,
                temperature=temperature,
                messages=messages
            )
            responses[model] = raw_response.choices[0].message.content

        else:
            print(f"Model {model} not found.")

    return responses
