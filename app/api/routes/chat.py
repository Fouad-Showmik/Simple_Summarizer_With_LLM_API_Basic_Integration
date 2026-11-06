from typing import Annotated

from fastapi import APIRouter, Depends

from app.clients.llm_client import LLMClient
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["chat"])


def get_chat_service():
    return ChatService(LLMClient())


ChatServiceDep = Annotated[ChatService, Depends(get_chat_service)]


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest, service: ChatServiceDep):
    return service.ask(request.message)
