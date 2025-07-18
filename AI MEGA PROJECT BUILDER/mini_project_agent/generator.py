import os
from groq import Groq
from dotenv import load_dotenv
from templates import get_project_prompt_template, CODE_ONLY_PROMPT_TEMPLATE
from utils import save_project

# Load environment variables from .env
load_dotenv()

# Initialize Groq client using API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Generate full B.Tech project (multi-file)
def generate_project_assets(domain: str, language: str):
    prompt = get_project_prompt_template(domain, language)
    
    chat_response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
        top_p= 0.95,
    )

    project_text = chat_response.choices[0].message.content.strip()
    project_title = f"{domain.title()}_{language.title()}_Project"

    save_project(project_title, project_text)
    return project_title, project_text


# (Optional) Generate just code module with lower temperature
def generate_code_only(domain: str, language: str):
    prompt = CODE_ONLY_PROMPT_TEMPLATE.format(domain=domain, language=language)
    
    code_response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    response_text = code_response.choices[0].message.content.strip()
    project_title = f"{domain.title()}_{language.title()}_CodeOnly"

    save_project(project_title, response_text)
    return project_title, response_text
