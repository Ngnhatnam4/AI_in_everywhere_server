import openai

async def chat_deepseek(data):
    openai.api_base = "https://api.deepseek.com"
    openai.api_key = data.get("api_key")
    messages = data.get("messages", [])
    response = openai.ChatCompletion.create(
        model=data.get("model", "deepseek-chat"),
        messages=messages
    )
    return response
