from fastapi import APIRouter, Request
from handlers.openai_handler import chat_openai
from handlers.claude_handler import chat_claude
from handlers.gemini_handler import chat_gemini
from handlers.mistral_handler import chat_mistral
from handlers.huggingface_handler import chat_hf
from handlers.deepseek_handler import chat_deepseek

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    model = data.get("model", "")
    if "gpt" in model:
        return await chat_openai(data)
    elif "claude" in model:
        return await chat_claude(data)
    elif "gemini" in model:
        return await chat_gemini(data)
    elif "mistral" in model:
        return await chat_mistral(data)
    elif "hf" in model:
        return await chat_hf(data)
    elif "deepseek" in model:
        return await chat_deepseek(data)
    else:
        return {"error": "Model not supported"}
