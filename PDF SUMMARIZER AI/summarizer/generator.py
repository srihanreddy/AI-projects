import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "deepseek-coder:latest"  # Or "llama3-70b-8192" or your chosen model


def summarize_chunks(chunks):
    summaries = []

    for chunk in chunks:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes academic PDFs into definitions, formulas, 2-mark and 5-mark points."},
                {"role": "user", "content": f"Summarize the following content:\n\n{chunk}"}
            ],
            temperature=0.3,
           max_tokens= 1500,
        )
        summary = response.choices[0].message.content.strip()
        summaries.append(summary)

    return "\n\n".join(summaries)
