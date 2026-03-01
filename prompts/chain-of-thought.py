# Chain of thought prompting
# Few shot prompting
# Directly giving the instructions to the model and few examples to the model.
# The model is provided with a few examples before asking it to generate a response.

from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
    Rules:
    - Strictly follow the given JSON output format
    - Only run once step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times)
    and finally OUTPUT (which is going to be displayed to the user).
    
    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}
    
    Example:
    START: Hey, can you solve 2+3*10/5 ?
    PLAN: {"step": "PLAN", "content": "Seems like user  is interested in maths problem"}
    PLAN: {"step": "PLAN", "content": "Looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN", "content": "First we must divide 10/5 which is 2"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2+3*2"}
    PLAN: {"step": "PLAN", "content": "Now we must multiply 3*2 which is 6"}
    PLAN: {"step": "PLAN", "content": "Now the equation is 2+6"}
    PLAN: {"step": "PLAN", "content": "We must perform the addition 2+6 which is equal to 8"}
    PLAN: {"step": "PLAN", "content": "Great, we have solved the problem and finally left with 8 as the answer."}
    OUTPUT: {"step": "OUTPUT", "content": "8"}
    
    
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]
user_query = input("")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=message_history
    )
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    if parsed_result.get("step") == "START":
        print(">>>>>> starting LLM Loop", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("???????? thinking", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("=====processing completed=====", parsed_result.get("content"))
    break

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, write a code to add n numbers in js"},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a JavaScript function to add 'n' numbers."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I need to write a JavaScript function that can accept an arbitrary number of arguments and return their sum."})},
#         {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I can achieve this using the rest parameter (...) to gather all arguments into an array and then use a loop or reduce method to sum them up."})}
#     ]
# )

# print(response.choices[0].message.content)

