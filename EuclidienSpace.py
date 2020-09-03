import numpy as np
from FunctionClass import Function

class EuclidienSpace:
    def __init__(self, plotInterval):
        self.plotInterval = plotInterval
        return

    def dotProduct(self, f, g):
        a, b = self.plotInterval
        return EuclidienSpace.__integral(a, b, (f*g).function)

    def norm(self, f):
        return np.sqrt(self.dotProduct(f, f))

    def orthoNormalise(self, vectors):
        result = [(1 / self.norm(vectors[0])) * vectors[0]]

        for i in range(1, len(vectors)):
            v = vectors[i] - self.projectOn(vectors[i], result)
            result.append((1 / self.norm(v)) * v)

        return result

    def projectOn(self, f, vectors):
        result = 0
        coordinates = []
        for i in range(len(vectors)):
             result += self.dotProduct(f, vectors[i]) * vectors[i]

        return result

    def getCoordinatesIn(self, f, vectors):
        result = []

        for i in range(len(vectors)):
            result.append(self.dotProduct(f, vectors[i]))

        return result

    @staticmethod
    def __integral(a, b, f, precision=10 ** (-4)):
        value = 0
        n = int(1 / precision)

        for k in range(n):
            value += f(a + k * (b - a) / n) * (b - a) / n

        return value