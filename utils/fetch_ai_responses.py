"""
Makes a request to each AI model and returns the response
"""
import asyncio
from config import settings


async def fetch_chatgpt(client, model, prompt):
    print(f"asking chatgpt...")
    raw_response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return "CHATGPT", raw_response.choices[0].message.content


async def fetch_gemini(client, model, prompt):
    print(f"asking gemini...")
    raw_response = await client.aio.models.generate_content(
        model=model,
        contents=prompt
    )
    return "GEMINI", raw_response.text


async def fetch_deepseek(client, model, prompt):
    print(f"asking deepseek...")
    raw_response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return "DEEPSEEK", raw_response.choices[0].message.content


async def fetch_claude(client, model, prompt):
    print(f"asking claude...")
    raw_response = await client.messages.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return "CLAUDE", raw_response.content[0].text.strip()


async def fetch_ai_responses(prompt):
    print(f"\n\nfetching ai responses using the following prompt:\n{prompt}")
    tasks = []

    for model_name, model_configuration in settings.AI_MODELS.items():
        client = model_configuration["client"]
        model = model_configuration["version"]

        if model_name == "CHATGPT":
            tasks.append(fetch_chatgpt(client, model, prompt))
        elif model_name == "GEMINI":
            tasks.append(fetch_gemini(client, model, prompt))
        elif model_name == "DEEPSEEK":
            tasks.append(fetch_deepseek(client, model, prompt))
        elif model_name == "CLAUDE":
            tasks.append(fetch_claude(client, model, prompt))
        else:
            print(f"{model_name} ai model not found.")

    results = await asyncio.gather(*tasks)

    responses = {}
    for result in results:
        model, response = result
        responses[model] = response

    return responses
