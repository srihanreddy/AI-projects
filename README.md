# 🎓 AI Projects by Srihan Reddy

A curated collection of practical AI tools and applications designed primarily for B.Tech students and learners. These projects use cutting-edge LLMs like DeepSeek-Coder and LLaMA 3 via Groq to automate real-world educational tasks and generate full-scale project assets.

---

## 📌 Projects Included

- **BTech Project Generator** – Auto-generates full B.Tech-level projects with code, documentation, presentations, and resume summaries.
- **PDF-to-Notes Summarizer** – Extracts key definitions, formulas, and short answers from textbooks or PDFs using LLMs.
- **Resume Project Builder** – AI agent that generates mini-projects tailored to Computer Science students for inclusion in resumes.

---

## 🚀 Key Features

- Multi-file Python project generation
- Automated generation of:
  - README.md
  - Project Report (DOC/PDF)
  - PPT Presentation
  - Resume Bullet Points
  - Sample input/output data
- Customizable by domain (AI, Web, IoT, ML, etc.)
- Powered by Groq API using high-speed LLMs

---

## 📁 Repository Structure

```
AI-projects/
├── .env
├── requirements.txt
├── README.md
├── btech_project_agent/
│   ├── mini_project_agent/
│   │   ├── agent.py
│   │   ├── generator.py
│   │   ├── formatter.py
│   │   ├── templates.py
│   │   └── utils.py
│   └── output/
├── pdf_to_notes_summarizer/
├── resume_project_builder/
└── tests/
    └── test_agent.py
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/srihanreddy/AI-projects.git
   cd AI-projects
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Groq API key to `.env`**
   ```
   GROQ_API_KEY=your_key_here
   ```

4. **Run the BTech Project Generator**
   ```bash
   cd btech_project_agent
   python mini_project_agent/agent.py
   ```

---

## 🧠 Domains Supported

- Artificial Intelligence
- Web Development
- Internet of Things (IoT)
- Machine Learning
- Cybersecurity (optional)

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Srihan Reddy**  
Passionate about building real-world AI tools that help students and engineers succeed.  
GitHub: [https://github.com/srihanreddy](https://github.com/srihanreddy)
