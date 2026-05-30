import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key) if api_key else None


def ask_ai_about_data(question: str, data_summary: str) -> str:
    if client is None:
        return "OpenAI API key not configured."

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
        model="gpt-4o-mini",
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