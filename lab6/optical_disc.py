class OpticalDisc:
    def __init__(self, capacity_mb: float, rpm: int, laser_thickness_nm: float):
        """
        capacity_mb — ёмкость диска в мегабайтах
        rpm — обороты в минуту
        laser_thickness_nm — толщина лазера в нанометрах
        """
        self.capacity_mb = capacity_mb
        self.rpm = rpm
        self.laser_thickness_nm = laser_thickness_nm

    def data_in_20_seconds(self):
        """
        По варианту:
        Сколько байт проходит лазер за 20 секунд.
        Каждая дорожка считается окружностью одинаковой длины.
        Допущение: объем равномерно распределён по поверхности.
        """

        bytes_total = self.capacity_mb * 1024 * 1024
        bytes_per_second = bytes_total / 60  # за 1 оборот — 1/60 объёма
        return bytes_per_second * 20

    def avg_rotation_time(self):
        """Среднее время одного оборота (в секундах)."""
        return 60 / self.rpm

    def __add__(self, other):
        """Перегрузка оператора сложения. Работает только для одинаковых типов дисков."""
        if type(self) is not type(other):
            raise TypeError("Сложение возможно только между объектами одного класса!")

        new_capacity = self.capacity_mb + other.capacity_mb
        new_rpm = self.rpm + other.rpm
        new_laser = (self.laser_thickness_nm + other.laser_thickness_nm) / 2

        return type(self)(
            new_capacity,
            new_rpm,
            new_laser
        )

    def info(self):
        return (
            f"Ёмкость: {self.capacity_mb} МБ\n"
            f"Обороты: {self.rpm} об/мин\n"
            f"Толщина лазера: {self.laser_thickness_nm} нм"
        )
