import string

PERS = string.ascii_uppercase + string.digits


def shift_right(ch, s):
    index = PERS.index(ch)
    return PERS[(index + s) % len(PERS)]


def shift_left(ch, s):
    index = PERS.index(ch)
    return PERS[(index - s) % len(PERS)]


def generate_key(prefix):
    prefix = prefix.strip().upper()

    if len(prefix) != 5 or not all(ch in PERS for ch in prefix):
        raise ValueError("Prefix must be exactly 5 symbols (A-Z, 0-9).")

    second = "".join(shift_right(ch, 3) for ch in prefix)
    third = "".join(shift_left(ch, 5) for ch in prefix)

    return f"{prefix}-{second}-{third}"
