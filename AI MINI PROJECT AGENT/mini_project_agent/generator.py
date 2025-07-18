import os
from dotenv import load_dotenv
from openai import OpenAI

# Load GROQ API key from .env
load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ✅ Generate full project content, title, viva
def generate_project_content(subject: str, topic: str, days: str):
    prompt = f"""
You are a helpful AI project assistant for engineering students.

Create a complete mini project in the field of "{topic}" using "{subject}".
It should be:
- Feasible in {days}
- Technically sound
- Realistic and complete

Respond in this format:
1. Project Title
2. Abstract
3. Tools/Technologies Used
4. Modules/Features
5. Estimated Completion Time
6. Viva Questions and Answers (at least 5)
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    result = response.choices[0].message.content.strip()

    # Extract title and viva section
    title = "Untitled Project"
    if "1. Project Title:" in result:
        title = result.split("1. Project Title:")[1].split("\n")[0].strip()
    elif result.startswith("1."):
        title = result.split("\n")[0].replace("1.", "").strip()

    viva_qna = ""
    if "6. Viva Questions" in result:
        viva_qna = result.split("6. Viva Questions")[1].strip()
    elif "6." in result:
        viva_qna = result.split("6.")[1].strip()

    return result, title, viva_qna

# ✅ Generate clean working code using DeepSeek
def generate_code_for_project(title: str, subject: str):
    prompt = f"""
You're an expert software engineer.

Write a fully working, beginner-friendly code for the following project in {subject}:
Project Title: {title}

Guidelines:
- Include all necessary syntax and logic
- Add comments to explain major steps
- Use only standard libraries (if possible)
- Code must be runnable in {subject} language
- Don't include explanations or markdown formatting. Just return code.

Start code below:
"""

    response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",  # ✅ Official Groq-supported DeepSeek model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
