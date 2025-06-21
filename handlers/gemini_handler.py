import google.generativeai as genai

async def chat_gemini(data):
    genai.configure(api_key=data.get("api_key"))
    model = genai.GenerativeModel(data.get("model", "gemini-pro"))
    chat = model.start_chat()
    response = chat.send_message(data["messages"][-1]["content"])
    return {"text": response.text}
