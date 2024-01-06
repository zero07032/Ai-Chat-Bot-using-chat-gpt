import openai


def answer(question):
    openai.api_key = ""
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
    )
    return completion.choices[0].message.content


