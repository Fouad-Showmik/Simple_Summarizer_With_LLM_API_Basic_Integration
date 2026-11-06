#Schemas(DTOs)

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(min_length= 100, max_length= 5000)


class ChatResponse(BaseModel):
    reply: str
    total_tokens: int