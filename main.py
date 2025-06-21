from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from keep_alive import keep_alive
from model_router import router
import uvicorn

app = FastAPI(title="AI API Server")
app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

keep_alive()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
