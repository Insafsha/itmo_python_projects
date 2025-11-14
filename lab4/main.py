from solver import solve_inventory
from inventory import build_inventory

def main():
    selected, _, score = solve_inventory()

    if selected is None:
        print("Итоговые очки выживания отрицательные!")
        return

    grid = build_inventory(selected)

    print("\nИнвентарь:")
    for row in grid:
        print(" ".join(f"[{c}]" for c in row))

    print(f"\nВыбранные предметы: {', '.join(selected)}")
    print(f"Итоговые очки выживания: {score}")


if __name__ == "__main__":
    main()
