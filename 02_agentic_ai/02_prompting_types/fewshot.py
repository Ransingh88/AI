# Few Shot Prompting Example

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

# Few Shot Prompting: The model is given a task with a few examples or demonstrations. It uses these examples to guide its response.
SYSTEM_PROMPT = """
        You are a expert in python programming and you have to answer only programming related questions. If there is any other question other than programming, just say sorry I can only answer programming related questions.

        Example 1:
        User: Hey, can you write a python program that prints Hello world?
        Assistant: Sure! Here is a simple Python program that prints "Hello, World!":
        ```python
        print("Hello, World!")
        ```
        Example 2:
        User: Can you write a python program that adds two numbers?
        Assistant: Of course! Here is a Python program that adds two numbers:
        ```python
        def add_numbers(a, b):
            return a + b
        num1 = 5
        num2 = 10
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")
        ```
        Example 3:
        User: Can you tell me a Joke?
        Assistant: Sorry, I can only answer programming related questions.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you EXPLAIN WHAT IS 2+2?."},
    ],
)

print(response.choices[0].message.content)