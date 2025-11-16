import os

def load_text(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()

def save_text(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
