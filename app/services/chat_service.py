# Business Logic
from app.clients.llm_client import LLMClient
from app.schemas.chat import ChatResponse


class ChatService:
    SYSTEM_PROMPT = (
        "You are a summarizer. The user's message is text to be summarized. "
        "Summarize it in 2 concise sentences. Do not ask questions."
    )  # instruction

    def __init__(self, client: LLMClient):  # Dependency Injection
        self.client = client

    def ask(self, user_message: str):
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ]

        data = self.client.complete(messages)

        return ChatResponse(
            reply=self._extract_text(data),
            total_tokens=data["usage"]["total_tokens"],
        )

    @staticmethod
    def _extract_text(data: dict):
        parts = []
        for item in data["output"]:
            if item["type"] == "message":
                for block in item["content"]:
                    if block["type"] == "output_text":
                        parts.append(block["text"])
        return "".join(parts)
