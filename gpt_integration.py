import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.environ["API_KEY"]
message = "What is book?"
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],
)

print("Answer==================================>", completion.choices[0])
