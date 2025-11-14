"""
Lab 1 — Flag of Lithuania using ANSI escape codes
"""

RED = '\x1b[48;5;196m'
YELLOW = '\x1b[48;5;220m'
GREEN = '\x1b[48;5;82m'
RESET = '\x1b[0m'

LENGTH = 40


def draw_line(color):
    line = ' ' * LENGTH
    print(color + line + RESET)


def flag_maker():
    for _ in range(6):
        draw_line(YELLOW)
    for _ in range(6):
        draw_line(GREEN)
    for _ in range(6):
        draw_line(RED)


if __name__ == "__main__":
    flag_maker()
