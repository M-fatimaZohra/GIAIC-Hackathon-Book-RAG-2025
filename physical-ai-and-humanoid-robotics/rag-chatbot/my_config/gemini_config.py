import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")

CLIENT = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)
# MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash", client=CLIENT) # Will be defined in course_agent.py
