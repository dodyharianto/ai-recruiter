"""Shared OpenAI key resolution for LangChain clients (allows app boot without a key)."""
import os


def openai_api_key_for_clients() -> str:
    key = (os.getenv("OPENAI_API_KEY") or "").strip()
    if key:
        return key
    # LangChain, CrewAI, and OpenAI clients read OPENAI_API_KEY from the environment.
    placeholder = "sk-placeholder-set-OPENAI_API_KEY"
    os.environ["OPENAI_API_KEY"] = placeholder
    return placeholder
