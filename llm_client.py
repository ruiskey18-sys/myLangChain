# 1. 创建 LLM

import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

llm = ChatOllama(
    model=os.getenv('LLM_MODEL_NAME'),
    base_url=os.getenv("LLM_BASE_URL"),
    temperature=0,
    num_ctx=4096
)

openai_client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]
