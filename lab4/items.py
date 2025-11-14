# Информация о предметах
ITEMS = {
    'rifle':     {'value': 25, 'volume': 3, 'char': 'r'},
    'pistol':    {'value': 15, 'volume': 2, 'char': 'p'},
    'ammo':      {'value': 15, 'volume': 2, 'char': 'a'},
    'medkit':    {'value': 20, 'volume': 2, 'char': 'm'},
    'inhaler':   {'value': 5,  'volume': 1, 'char': 'i'},   # обязательно
    'knife':     {'value': 15, 'volume': 1, 'char': 'k'},
    'axe':       {'value': 20, 'volume': 3, 'char': 'x'},
    'talisman':  {'value': 25, 'volume': 1, 'char': 't'},
    'flask':     {'value': 15, 'volume': 1, 'char': 'f'},
    'antidot':   {'value': 10, 'volume': 1, 'char': 'd'},
    'supplies':  {'value': 20, 'volume': 2, 'char': 's'},
    'crossbow':  {'value': 20, 'volume': 2, 'char': 'c'},
}

# Данные варианта №5
ROWS = 2
COLS = 4
MAX_VOL = ROWS * COLS
START_POINTS = 20

# Условие болезни — астма → ингалятор обязателен
REQUIRED_ITEM = "inhaler"
