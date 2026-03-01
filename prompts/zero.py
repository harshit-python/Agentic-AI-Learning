# Zero shot prompting
# The model is given direct question or task without prior examples.

from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()


client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting : Directly giving the instructions to the model
SYSTEM_PROMPT = """You should only and only answer the coding related questions. 
Do not answer anything else. 
Your name is Alexa. If user asks anything other than coding, just say sorry."""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "can you write a python code to translate the world hello to hindi"}
    ]
)

print(response.choices[0].message.content)