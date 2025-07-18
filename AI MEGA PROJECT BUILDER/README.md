# 🎓 AI BTech Project Generator

A powerful AI agent that generates complete B.Tech-level projects—source code, documentation, reports, presentations, and resume points—using Groq's high-speed LLMs like DeepSeek-Coder and LLaMA 3.

---

## 🚀 Features

- Multi-file Python code generation
- Auto-generated:
  - README
  - Final-year Report
  - PPT Presentation
  - Resume Bullet Points
  - Input/Output samples
- Supports domains like AI, Web, IoT, ML, etc.
- Customizable by domain & language

---

## 📁 Folder Structure

```
btech_project_agent/
├── .env
├── requirements.txt
├── README.md
├── mini_project_agent/
│   ├── agent.py
│   ├── generator.py
│   ├── formatter.py
│   ├── templates.py
│   └── utils.py
├── output/
│   └── [auto-generated project folders]
└── tests/
    └── test_agent.py
```

---

## ⚙️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/srihanreddy/AI-projects
   cd AI-projects/btech_project_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Groq API key to `.env`:
   ```
   GROQ_API_KEY=your_key_here
   ```

4. Run the agent:
   ```bash
   python mini_project_agent/agent.py
   ```

---

## 🧪 Example Domains

- Artificial Intelligence
- Web Development
- IoT Projects
- Cybersecurity
- Data Science

---

## 📄 License

MIT License

---

## 👨‍💻 Author

[Srihan Reddy](https://github.com/srihanreddy)
