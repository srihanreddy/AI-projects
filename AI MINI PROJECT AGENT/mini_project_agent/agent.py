import os
from generator import generate_project_content, generate_code_for_project
from formatter import save_all_formats, save_code_files, save_viva_only
from utils import estimate_time, zip_project

def main():
    print("🎓 Welcome to Mini Project Generator (Groq-powered)\n")

    subject = input("📘 Enter subject (e.g., Python, Java): ").strip()
    topic = input("🧠 Enter topic/domain (e.g., IoT, AI, ML): ").strip()
    days = input("⏱️ Enter time available to complete the project (default: 3 days): ").strip() or "3"

    print(f"\n⚙️ Generating project on '{topic}' using {subject}...\n")

    content, title, viva_qna = generate_project_content(subject, topic, days)
    code = code = generate_code_for_project(title, subject)


    base = os.path.join("output", topic.lower().replace(" ", "_"))
    save_all_formats(content, viva_qna, code, base, subject)
    save_code_files(code, base, subject)
    save_viva_only(viva_qna, base)

    print("\n🧠 Estimated Completion Time:", estimate_time(content))
    zip_project(base)

    print(f"\n✅ All files saved in: {base}")
    print(f"📦 Project ZIP archive: {base}.zip")

if __name__ == "__main__":
    main()
