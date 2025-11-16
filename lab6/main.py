from paddle_boat import PaddleBoat
from motor_boat import MotorBoat

def main():
    boat1 = PaddleBoat("Рыбачок", max_speed=8, capacity=3, paddles=2)
    boat2 = MotorBoat("Шторм", max_speed=25, capacity=4, engine_power=90)

    print("--- Лодка на вёслах ---")
    print(boat1.info(), "\n")

    print("--- Лодка с мотором ---")
    print(boat2.info(), "\n")

    print("--- Перегрузка оператора + ---")
    mixed = boat1 + boat2
    print(mixed.info())

if __name__ == "__main__":
    main()
