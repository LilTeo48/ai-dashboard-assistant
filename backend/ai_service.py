import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_ai_about_data(question: str, data_summary: str) -> str:

    prompt = f"""
    You are an AI data analyst assistant.

    The user is asking questions about this sales dataset:

    {data_summary}

    User question:
    {question}

    Give a clear, beginner-friendly business insight.
    Keep it concise.
    """

    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {
                "role": "system",
                "content": "You explain business data clearly."
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
    