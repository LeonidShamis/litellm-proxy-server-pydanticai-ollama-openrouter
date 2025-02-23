# https://ai.pydantic.dev/models/#example-using-a-remote-server

from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

import os
from dotenv import load_dotenv


load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3.2:3b-instruct-q8_0")

OLLAMA_BASE_URL = "http://" + OLLAMA_HOST + ":11434/v1"


ollama_model = OpenAIModel(
    model_name=OLLAMA_MODEL_NAME,
    base_url=OLLAMA_BASE_URL,
    api_key = 'api-key-not-set',
)


class CityLocation(BaseModel):
    city: str
    country: str


agent = Agent(model=ollama_model, result_type=CityLocation)

result = agent.run_sync('Where were the olympics held in 2012?')
print(result.data)
#> city='London' country='United Kingdom'
print(result.usage())
"""
Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
"""