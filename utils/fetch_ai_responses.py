"""
Makes a request to each AI model and returns the response
"""
from config import settings


def fetch_ai_responses(prompt):
    # fetch_ai_responses should return {model_name: ai_result_string}
    responses: dict[str, str] = {}

    for model_name, model_configuration in settings.AI_MODELS.items():
        model = model_name
        version = model_configuration["version"]
        max_tokens = model_configuration["max_tokens"]
        temperature = model_configuration["temperature"]
        client = model_configuration["client"]
        messages = [{"role": "user", "content": prompt}]

        # fetch chatgpt response
        if model == "CHATGPT":
            print(f"asking chatgpt...")
            raw_response = client.chat.completions.create(
                model=version,
                temperature=temperature,
                messages=messages
            )
            responses[model] = raw_response.choices[0].message.content

        # fetch gemini response
        elif model == "GEMINI":
            print(f"asking gemini...")
            raw_response = client.models.generate_content(
                model=version,
                contents=prompt
            )
            responses[model] = raw_response.text

        # fetch deepseek response
        elif model == "DEEPSEEK":
            print(f"asking deepseek...")
            raw_response = client.chat.completions.create(
                model=version,
                temperature=temperature,
                messages=messages
            )
            responses[model] = raw_response.choices[0].message.content

        # fetch claude response
        elif model == "CLAUDE":
            print(f"asking claude...")
            raw_response = client.messages.create(
                model=version,
                max_tokens=max_tokens,
                messages=messages
            )
            responses[model] = raw_response.content[0].text.strip()

        else:
            print(f"{model} ai model not found.")

    return responses
