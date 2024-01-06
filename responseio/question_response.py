import openai


def answer(question):
    openai.api_key = "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"
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


