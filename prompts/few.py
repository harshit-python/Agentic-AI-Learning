# Few shot prompting
# Directly giving the instructions to the model and few examples to the model.
# The model is provided with a few examples before asking it to generate a response.

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()


client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You should only and only answer the coding related questions. 
Do not answer anything else. 
Your name is Alexa. If user asks anything other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON Format

Output Format:
{{
"code": "string" or None,
"isCodingQuestion": boolean
}}

Examples:
Question: Can you explain the a+b whole square?
Answer: {{
    "code": null, 
    "isCodingQuestion": false
    }}

Question: Hey, write a python code to add 2 numbers.
Answer: {{
    "code": "def add(a,b):
                return a+b", 
    "isCodingQuestions": true
    }}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "can you write a python code to add 2 numbers a and b?"}
    ]
)

print(response.choices[0].message.content)