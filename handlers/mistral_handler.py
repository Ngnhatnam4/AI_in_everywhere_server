from mistralai.client import MistralClient

async def chat_mistral(data):
    client = MistralClient(api_key=data.get("api_key"))
    model = data.get("model", "mistral-tiny")
    messages = data.get("messages", [])
    response = client.chat(model=model, messages=messages)
    return response
