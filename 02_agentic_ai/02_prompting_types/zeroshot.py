# Zero Shot Prompting Example

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

# Zero Shot Prompting: The model is given a task without any examples or demonstrations. It relies solely on the instructions provided in the prompt to generate a response.
SYSTEM_PROMPT = "You are a expert in pythonic programming and you have to answer only programming related questions. If there is any other question other than programming, just say sorry I can only answer programming related questions."

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you write a python program that prints Hello world?."},
    ],
)

print(response.choices[0].message.content)