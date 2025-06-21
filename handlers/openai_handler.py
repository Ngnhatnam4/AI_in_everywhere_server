import openai

async def chat_openai(data):
    openai.api_key = data.get("api_key")
    messages = data.get("messages", [])
    model = data.get("model", "gpt-3.5-turbo")

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=2048
    )
    return response
