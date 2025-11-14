"""
Lab 1 — Analysis of numeric sequence (even/odd index average comparison)
"""

WHITE = '\x1b[48;5;15m'
RESET = '\x1b[0m'


def load_sequence():
    with open("sequence.txt") as f:
        return [abs(float(x)) for x in f]


def split_even_odd(numbers):
    even = [x for i, x in enumerate(numbers) if i % 2 == 0]
    odd = [x for i, x in enumerate(numbers) if i % 2 == 1]
    return even, odd


def averages(even, odd):
    avg_even = sum(even) / len(even)
    avg_odd = sum(odd) / len(odd)
    overall = (sum(even) + sum(odd)) / (len(even) + len(odd))
    return avg_even / overall, avg_odd / overall


def draw_chart(even_label, odd_label):
    max_height = int(max(even_label, odd_label) * 10)
    for h in range(max_height, 0, -1):
        left = WHITE + " " if h < even_label * 10 else " "
        right = WHITE + " " if h < odd_label * 10 else " "
        print(" " * 10 + left + RESET + " " * 20 + right + RESET)


if __name__ == "__main__":
    nums = load_sequence()
    even, odd = split_even_odd(nums)
    even_label, odd_label = averages(even, odd)

    draw_chart(even_label, odd_label)

    print(f"\nЧётные индексы:  {even_label:.3f}")
    print(f"Нечётные индексы: {odd_label:.3f}")
