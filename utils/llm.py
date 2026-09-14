import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def get_llm():
    return ChatOllama(
        model=os.getenv("MODEL_NAME", "llama3.2:latest"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.3
    )
