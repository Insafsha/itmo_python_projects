from optical_disc import OpticalDisc

class CD(OpticalDisc):
    def __init__(self, capacity_mb, rpm, laser_thickness_nm, diameter_cm=12):
        super().__init__(capacity_mb, rpm, laser_thickness_nm)
        self.diameter_cm = diameter_cm   # уникальное поле

    def info(self):
        base = super().info()
        return base + f"\nДиаметр: {self.diameter_cm} см\nТип: CD"
