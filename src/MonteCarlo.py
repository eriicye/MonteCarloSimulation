import math
import numpy as np

class MonteCarlo:
    def __init__(self) -> None:
        self.circle_area = math.pi
        self.rectangle_area = 4

        self.rng = np.random.default_rng()
        self.x_array = np.array([])
        self.y_array = np.array([])
        self.hypotenuse = np.array([])

        self.in_circle = 0
        self.outside_circle = 0


    def calculate(self, amount) -> None:
        self.x_array = self.rng.uniform(low=0, high=2, size=amount)
        self.y_array = self.rng.uniform(low=0, high=2, size=amount)

        np.square(self.x_array)
        np.square(self.y_array)

        self.hypotenuse = np.sqrt(self.x_array + self.y_array)


