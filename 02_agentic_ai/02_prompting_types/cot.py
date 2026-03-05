# Chain of Thought Prompting Example

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # Load environment variables from .env file

client = OpenAI()

# Chain of Thought Prompting: The model is given a task and is asked to think through the problem step by step before providing the final answer.
SYSTEM_PROMPT = """
        You are a expert AI assistant in resolving user queries using chain of thought prompting. You will be given a question and you have to think step by step to arrive at the final answer.
        You work on START, PLAN and OUTPUT steps. In START step, you will restate the question and identify the key components of the problem. In PLAN step, you will outline a strategy to solve the problem, breaking it down into smaller, manageable steps. In OUTPUT step, you will execute the plan and provide the final answer.

        Rules:
        1. Always follow the START, PLAN, OUTPUT steps in order.
        2. Strictly floow the given JSON format.
        3. Run one step at a time and wait for the next instruction before proceeding to the next step.
        4. If you are unsure about any step, ask for clarification before proceeding.

        Output JSON Format:
            {{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}}
        
        Example:
        START: Hey, can you solve 2+3*5/10?
        PLAN: {"step": "PLAN", "content": "The question is asking to solve the expression 2+3*5/10. The key components of the problem are the numbers 2, 3, 5, and 10, and the operations of addition, multiplication, and division."}
        PLAN: {"step": "PLAN", "content": "To solve the expression, we will follow the order of operations (PEMDAS/BODMAS). First, we will solve the multiplication and division from left to right, and then we will solve the addition."}
        PLAN: {"step": "PLAN", "content": "First, we will solve the multiplication: 3*5 = 15."}
        PLAN: {"step": "PLAN", "content": "Then we will solve the division: 15/10 = 1.5."}
        PLAN: {"step": "PLAN", "content": "Finally, we will solve the addition: 2 + 1.5 = 3.5."}
        OUTPUT: {"step": "OUTPUT", "content": "The final answer is 3.5."}
"""

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

user_input = input("[ ]: ")
message_history.append({"role": "user", "content": user_input})
print(f"Thinking...")
while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_content = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_content})
    parsed_content = json.loads(raw_content)  # Parse the JSON content from the response

    if parsed_content.get("step") == "START" or parsed_content.get("step") == "PLAN":
        print(f"- {parsed_content.get('content')}")
        continue
    elif parsed_content.get("step") == "OUTPUT":
        print(f"OUTPUT: {parsed_content.get('content')}")
        break
