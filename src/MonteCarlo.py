import math
import numpy as np

class MonteCarlo:
    def __init__(self) -> None:
        self.rng = np.random.default_rng()
        self.x_array = np.array([])
        self.y_array = np.array([])
        self.hypotenuse = np.array([])

        self.in_circle = 0
        self.outside_circle = 0

        self.answer = 0.0 # pi approximation


    def calculate(self, amount) -> float:
        self.x_array = self.rng.uniform(low=0, high=2, size=amount)
        self.y_array = self.rng.uniform(low=0, high=2, size=amount)

        self.x_array = np.abs(self.x_array - 1)
        self.y_array = np.abs(self.y_array - 1)

        np.square(self.x_array)
        np.square(self.y_array)

        self.hypotenuse = np.sqrt(self.x_array + self.y_array)

        self.in_circle = self.hypotenuse[self.hypotenuse < 1]
        self.outside_circle = self.hypotenuse[self.hypotenuse > 1]

        self.answer = (len(self.in_circle) / len(self.outside_circle)) * 4

        return self.answer