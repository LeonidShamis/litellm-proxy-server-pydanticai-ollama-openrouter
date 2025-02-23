# https://docs.litellm.ai/docs/providers/litellm_proxy#usage---streaming

from litellm import completion

import os
from dotenv import load_dotenv

load_dotenv()

LITELLM_PROXY_API_KEY = os.getenv("LITELLM_PROXY_API_KEY")
LITELLM_PROXY_API_BASE = os.getenv("LITELLM_PROXY_API_BASE", "http://localhost:4000")
LITELLM_PROXY_MODEL_NAME = os.getenv("LITELLM_PROXY_MODEL_NAME")

assert(LITELLM_PROXY_API_KEY)
assert(LITELLM_PROXY_MODEL_NAME)

messages = [
        { "content": "Write a poem about coding in 10 words", "role": "user"}
    ]

# litellm proxy call
try:
    response = completion(
            model="litellm_proxy/" + LITELLM_PROXY_MODEL_NAME, 
            messages=messages,
            api_base=LITELLM_PROXY_API_BASE,
            api_key=LITELLM_PROXY_API_KEY,
            stream=True
        )

    for chunk in response:
        print(chunk)
except Exception as ex:
    print(ex)
