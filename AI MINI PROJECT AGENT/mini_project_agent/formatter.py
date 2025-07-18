import os

# 📄 Save project description as text
def save_project_description(content: str, base_path: str):
    os.makedirs(base_path, exist_ok=True)
    with open(os.path.join(base_path, "project_description.txt"), "w", encoding="utf-8") as f:
        f.write(content)

# 🧠 Save viva questions separately
def save_viva_questions(questions: str, base_path: str):
    os.makedirs(base_path, exist_ok=True)
    with open(os.path.join(base_path, "viva_questions.txt"), "w", encoding="utf-8") as f:
        f.write(questions)

# 🧠 Save only viva content (alias)
def save_viva_only(questions: str, base_path: str):
    save_viva_questions(questions, base_path)

# 📁 Get file extension based on subject/language
def get_file_extension(subject: str) -> str:
    extensions = {
        "python": "py",
        "java": "java",
        "c++": "cpp",
        "c": "c",
        "c#": "cs",
        "javascript": "js",
        "html": "html",
        "css": "css",
        "kotlin": "kt",
        "go": "go",
        "typescript": "ts"
    }
    return extensions.get(subject.lower(), "txt")  # fallback to .txt

# 💾 Save code with language-specific extension
def save_code_files(code: str, base_path: str, subject: str):
    os.makedirs(base_path, exist_ok=True)
    ext = get_file_extension(subject)
    code_path = os.path.join(base_path, f"main.{ext}")
    with open(code_path, "w", encoding="utf-8") as f:
        f.write(code)

# ✅ Save all outputs in one go (description, viva, and code)
def save_all_formats(content: str, viva_qna: str, code: str, base_path: str, subject: str):
    save_project_description(content, base_path)
    save_viva_questions(viva_qna, base_path)
    save_code_files(code, base_path, subject)
