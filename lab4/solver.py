from items import ITEMS, MAX_VOL, START_POINTS, REQUIRED_ITEM


def solve_inventory():
    names = list(ITEMS.keys())
    n = len(names)

    # DP-таблица
    dp = [[0] * (MAX_VOL + 1) for _ in range(n)]

    # Заполнение таблицы
    for i, name in enumerate(names):
        value = ITEMS[name]['value']
        vol = ITEMS[name]['volume']

        for cap in range(1, MAX_VOL + 1):
            if i == 0:
                dp[i][cap] = 0 if vol > cap else value
            else:
                without_item = dp[i - 1][cap]
                with_item = dp[i - 1][cap - vol] + value if cap >= vol else 0
                dp[i][cap] = max(without_item, with_item)

    # Восстановление выбранных предметов
    selected = []
    cap = MAX_VOL

    for i in range(n - 1, -1, -1):
        if i == 0:
            if dp[i][cap] > 0:
                selected.append(names[i])
        else:
            if dp[i][cap] != dp[i - 1][cap]:
                selected.append(names[i])
                cap -= ITEMS[names[i]]['volume']

    # Обязательный предмет
    if REQUIRED_ITEM not in selected:
        selected.append(REQUIRED_ITEM)

    # Подсчёт итоговых очков
    score = START_POINTS
    for name in names:
        if name in selected:
            score += ITEMS[name]['value']
        else:
            score -= ITEMS[name]['value']

    if score <= 0:
        return None, None, score

    return selected, cap, score
