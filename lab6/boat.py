class Boat:
    def __init__(self, name: str, max_speed: float, capacity: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def info(self):
        return (
            f"Лодка: {self.name}\n"
            f"Макс. скорость: {self.max_speed} км/ч\n"
            f"Вместимость: {self.capacity} человек"
        )

    # Перегрузка оператора + 
    # Складываем скорости двух лодок как «комбинированную производительность»
    def __add__(self, other):
        if not isinstance(other, Boat):
            return NotImplemented

        return CombinedBoat(self, other)


class CombinedBoat:
    """Лодка, которая возникает при сложении двух лодок"""

    def __init__(self, boat1: Boat, boat2: Boat):
        self.boat1 = boat1
        self.boat2 = boat2
        self.total_speed = boat1.max_speed + boat2.max_speed
        self.total_capacity = boat1.capacity + boat2.capacity

    def info(self):
        return (
            f"Комбинированная лодка:\n"
            f" - {self.boat1.name}\n"
            f" - {self.boat2.name}\n\n"
            f"Суммарная скорость: {self.total_speed} км/ч\n"
            f"Суммарная вместимость: {self.total_capacity} человек"
        )
