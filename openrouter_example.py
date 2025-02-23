# https://ai.pydantic.dev/models/#openrouter

from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

import os
from dotenv import load_dotenv


load_dotenv()


OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL_NAME = os.getenv("OPENROUTER_MODEL_NAME", "google/gemini-2.0-flash-lite-preview-02-05:free")

assert(OPENROUTER_API_KEY)

model = OpenAIModel(
    model_name=OPENROUTER_MODEL_NAME,
    base_url=OPENROUTER_BASE_URL,
    api_key=OPENROUTER_API_KEY,
)

class CityLocation(BaseModel):
    city: str
    country: str

agent = Agent(
            model=model, 
            # headers={
            #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            # },
            result_type=CityLocation)

result = agent.run_sync('Where were the olympics held in 2012?')
print(result.data)
#> city='London' country='United Kingdom'
print(result.usage())
"""
Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
"""