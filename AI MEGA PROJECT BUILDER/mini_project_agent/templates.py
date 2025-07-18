def get_project_prompt_template(domain: str, language: str) -> str:
    return f"""
You are an expert B.Tech project builder and software architect.

Generate a **complete, production-grade, final-year B.Tech project** in the domain: "{domain}" using the language: "{language}".

🔧 **Requirements**:
- Code must be clean, modular, secure, and efficient.
- Use **industry-standard libraries** and **modern architecture**.
- Emphasize testability, maintainability, and reusability.
- Add **docstrings**, meaningful comments, and type hints (if supported by {language}).
- Follow standard naming conventions and best practices.

🔍 **Structure to Follow**:

1. <<<README.md>>> – Project overview, setup, features, tech stack, usage.
2. <<<main.{get_file_extension(language)}>>> – Entry point with CLI/GUI/Web init.
3. <<<modules/core_logic.{get_file_extension(language)}>>> – Main algorithm/processing logic.
4. <<<modules/ui.{get_file_extension(language)}>>> – UI code (CLI/GUI/Web).
5. <<<modules/utils.{get_file_extension(language)}>>> – Utility/helper methods.
6. <<<modules/data_handler.{get_file_extension(language)}>>> – File/DB/API data logic.
7. <<<modules/config.{get_file_extension(language)}>>> – Config/constants/env handler.
8. <<<modules/api.{get_file_extension(language)}>>> – API clients or backend endpoints (REST/FastAPI/etc.).
9. <<<{get_dependencies_filename(language)}>>> – Dependency/build file with comments.
10. <<<Dockerfile>>> – (Optional) Docker container setup.
11. <<<.env>>> – Env variables like API keys, DB configs.
12. <<<schema.sql>>> – DB schema (if applicable).
13. <<<report.md>>> – Report: Abstract, objectives, design, architecture, testing.
14. <<<ppt.md>>> – PPT structure: title, problem, solution, demo, future scope.
15. <<<resume.txt>>> – Resume bullet points for the project.
16. <<<input_samples/input1.txt>>> – Sample input data.
17. <<<output_samples/output1.txt>>> – Sample output.
18. <<<tests/test_main.{get_file_extension(language)}>>> – Unit tests for core modules.

⚠️ **Instructions**:
- Wrap filenames using <<<filename>>> exactly.
- All source code must be in ```{language} code blocks.
- Only output what is listed above.
- Use only {language} for source files.
"""


def get_file_extension(language: str) -> str:
    ext_map = {
        "python": "py",
        "java": "java",
        "c++": "cpp",
        "c": "c",
        "javascript": "js",
        "typescript": "ts",
        "go": "go",
        "rust": "rs",
        "php": "php"
    }
    return ext_map.get(language.lower(), "txt")

def get_dependencies_filename(language: str) -> str:
    dep_map = {
        "python": "requirements.txt",
        "java": "pom.xml",
        "c++": "CMakeLists.txt",
        "c": "Makefile",
        "javascript": "package.json",
        "typescript": "package.json",
        "go": "go.mod",
        "rust": "Cargo.toml",
        "php": "composer.json"
    }
    return dep_map.get(language.lower(), "dependencies.txt")

CODE_ONLY_PROMPT_TEMPLATE = """
You are a coding assistant. Write a complete {language} program based on this idea:

"{idea}"

Return only the complete code inside a single markdown code block.
"""
