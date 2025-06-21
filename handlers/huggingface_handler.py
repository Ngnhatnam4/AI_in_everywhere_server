from huggingface_hub import InferenceClient

async def chat_hf(data):
    client = InferenceClient(token=data.get("api_key"))
    model = data.get("model", "HuggingFaceH4/zephyr-7b-beta")
    prompt = data.get("messages", [{"content": ""}])[-1]["content"]
    response = client.text_generation(model=model, prompt=prompt)
    return {"text": response}
