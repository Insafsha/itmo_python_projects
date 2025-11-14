from items import ITEMS, ROWS, COLS


def build_inventory(selected):
    total_cells = ROWS * COLS
    inv = ["."] * total_cells
    pos = 0

    for name in selected:
        char = ITEMS[name]['char']
        for _ in range(ITEMS[name]['volume']):
            if pos < total_cells:
                inv[pos] = char
                pos += 1

    grid = [inv[i:i + COLS] for i in range(0, total_cells, COLS)]
    return grid
