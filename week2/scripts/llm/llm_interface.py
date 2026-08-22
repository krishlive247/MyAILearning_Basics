from abc import ABC, abstractmethod
from typing import Optional
import ollama
from openai import OpenAI

class LLMInterface(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass
    
    @abstractmethod
    def get_info(self) -> dict:
        pass

class OllamaLLM(LLMInterface):
    def __init__(self, model="llama2"):
        self.model = model
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            stream=False,
            options=kwargs
        )
        return response['response'].strip()
    
    def get_info(self) -> dict:
        return {"type": "Ollama", "model": self.model}

class OpenAILLM(LLMInterface):
    def __init__(self, model="gpt-3.5-turbo", api_key=None):
        self.model = model
        self.client = OpenAI(api_key=api_key)
    
    def generate(self, prompt: str, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response.choices[0].message.content.strip()
    
    def get_info(self) -> dict:
        return {"type": "OpenAI", "model": self.model}

class LLMFactory:
    @staticmethod
    def create(backend: str, **kwargs):
        if backend.lower() == "ollama":
            return OllamaLLM(**kwargs)
        elif backend.lower() == "openai":
            return OpenAILLM(**kwargs)
        else:
            raise ValueError(f"Unknown backend: {backend}")