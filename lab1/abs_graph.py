"""
Lab 1 — ASCII graph for y = |x|
"""

WHITE = '\x1b[48;5;15m'
RESET = '\x1b[0m'

W = 10  # width of the graph


def draw_pixel(offset):
    print(" " * offset + WHITE + " " + RESET)


def graph():
    for i in range(16, 8, -1):
        draw_pixel(i)


def graph2(width):
    for i in range(width):
        draw_pixel(i)


if __name__ == "__main__":
    print("\n\n#2 График |x|")
    graph()
    # дополнительные позиционирующие escape-коды (как в твоём оригинале):
    print('\u001b[10C')
    print('\u001b[10A')
    graph2(W)

    print("\n\n")
