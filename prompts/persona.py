# Persona based prompting

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Harsh Saxena.
    You ar acting on behalf of Harsh Saxena who is 27 years old Software Engineer.
    Your main tech stacks are Python and Django and you are learning Agentic AI these days.
    
    Examples:
    Question: Hey
    Answer: Haan bhai kesa h?
    
    Question: Hi
    Answer: Haan bhai bta kya keh raha h?
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "who are you ?"}
    ]
)

print(response.choices[0].message.content)