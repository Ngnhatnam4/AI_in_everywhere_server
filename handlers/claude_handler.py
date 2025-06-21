import anthropic

async def chat_claude(data):
    client = anthropic.Anthropic(api_key=data.get("api_key"))
    messages = data.get("messages", [])
    model = data.get("model", "claude-3-sonnet-20240229")
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=0.7,
        messages=messages
    )
    return response
