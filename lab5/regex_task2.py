import re
from utils import load_text, save_text

def solve_task2(path: str, output: str):
    text = load_text(path)

    # Вариант 5: извлечь все строки внутри content="..."
    contents = re.findall(r'content="([^"]+)"', text)

    save_text(output, "\n".join(contents))
