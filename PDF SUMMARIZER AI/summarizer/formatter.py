def save_summary(summary: str, path: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(summary)
