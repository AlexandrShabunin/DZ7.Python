class Road:
    weight = 20
    thickness = 0.1

    def __init__(self, length, width):
        self._length = length  # длина в метрах
        self._width = width  # ширина в метрах

    def mass_calcul(self):
        print(
            f'Масса асфальта составляет: '
            f'{((self._length * self._width * self.weight * self.thickness) / 1000)} '
            f'т')


instance = Road(20, 5000)
instance.mass_calcul()
