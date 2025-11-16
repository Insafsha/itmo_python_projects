from cd import CD
from dvd import DVD

def main():
    cd1 = CD(capacity_mb=700, rpm=480, laser_thickness_nm=780)
    dvd1 = DVD(capacity_mb=4700, rpm=1600, laser_thickness_nm=650, layers=2)

    print("=== CD ===")
    print(cd1.info())
    print("Данных проходит за 20 секунд:", int(cd1.data_in_20_seconds()), "байт")
    print("Среднее время оборота:", cd1.avg_rotation_time(), "сек\n")

    print("=== DVD ===")
    print(dvd1.info())
    print("Данных проходит за 20 секунд:", int(dvd1.data_in_20_seconds()), "байт")
    print("Среднее время оборота:", dvd1.avg_rotation_time(), "сек\n")

    print("=== Сложение двух CD ===")
    cd_sum = cd1 + CD(500, 300, 780)
    print(cd_sum.info())

if __name__ == "__main__":
    main()
