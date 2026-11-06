import requests

from app.core.config import settings

#talk to the provider over HTTP and return raw JSON.

class LLMClient: 
    def __init__(self):
        self.url = f"{settings.llm_base_url}/responses"
        self.headers = {
            "Authorization": f"Bearer {settings.llm_api_key}",
            "Content-Type": "application/json",
        }

    def complete(self, messages: list[dict]):
        payload = {
            "model" : settings.model_name,
            "input" : messages,
        }

        response = requests.post(self.url, headers=self.headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()