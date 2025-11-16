from optical_disc import OpticalDisc

class DVD(OpticalDisc):
    def __init__(self, capacity_mb, rpm, laser_thickness_nm, layers=1):
        super().__init__(capacity_mb, rpm, laser_thickness_nm)
        self.layers = layers   # уникальное поле

    def avg_rotation_time(self):
        """
        Вариант: среднее время одного оборота с учётом слоёв.
        Чем больше слоёв — тем дольше считывание.
        """
        return (60 / self.rpm) * self.layers

    def info(self):
        base = super().info()
        return base + f"\nКол-во слоёв: {self.layers}\nТип: DVD"
