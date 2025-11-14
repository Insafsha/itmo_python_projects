"""
Lab 1 — Symmetric block figure
"""

WHITE = '\x1b[48;5;15m'
RESET = '\x1b[0m'


def figure():
    j = 0
    k = 55
    for i in range(10, 1, -1):
        left = " " * j
        middle = WHITE + " " * (i + 1) + RESET
        right = WHITE + " " * (i + 1) + RESET
        space = " " * (k * 2 - i * 2)
        print(left + middle + space + right)
        j += i
        k -= i

    print(" " * 55 + WHITE + " " * 5 + RESET)
    print(" " * 57 + WHITE + " " + RESET)


if __name__ == "__main__":
    figure()
