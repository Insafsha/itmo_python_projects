from boat import Boat

class PaddleBoat(Boat):
    def __init__(self, name: str, max_speed: float, capacity: int, paddles: int):
        super().__init__(name, max_speed, capacity)
        self.paddles = paddles

    def info(self):
        base = super().info()
        return base + f"\nТип: весельная лодка\nКол-во вёсел: {self.paddles}"
