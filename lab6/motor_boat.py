from boat import Boat

class MotorBoat(Boat):
    def __init__(self, name: str, max_speed: float, capacity: int, engine_power: float):
        super().__init__(name, max_speed, capacity)
        self.engine_power = engine_power  # лошадиные силы

    def info(self):
        base = super().info()
        return base + f"\nТип: моторная лодка\nМощность двигателя: {self.engine_power} л.с."
