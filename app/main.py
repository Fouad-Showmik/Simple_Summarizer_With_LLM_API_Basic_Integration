from fastapi import FastAPI

from app.api.routes import chat

app = FastAPI(title="Simple Summarizer With Basic LLM API Integration", swagger_ui_parameters= {"defaultModelsExpandDepth": -1})
app.include_router(chat.router)