import numpy as np
import matplotlib.pyplot as plt


class Function:
    def __init__(self, function, plotInterval=[-10, 10]):
        self.function = function
        self.plotInterval = plotInterval
        return

    def __add__(self, other):
        def result(x):
            if isinstance(other, Function):
                return self.function(x) + other.function(x)

            return self.function(x) + other

        return Function(result, self.plotInterval)

    def __mul__(self, other):
        def result(x):
            if isinstance(other, Function):
                return other.function(x) * self.function(x)

            return other * self.function(x)

        return Function(result, self.plotInterval)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self + (-1) * other

    def __rsub__(self, other):
        return (-1) * self + other

    def __str__(self):
        a, b = self.plotInterval
        x = np.linspace(a, b, (b-a) * 10)

        plt.plot(x, self.function(x))
        plt.grid()
        plt.show()
        return "See the graph."

    @staticmethod
    def plotFunctions(*args):
        a, b = args[0].plotInterval

        for func in args:
            if a <= func.plotInterval[0]:
                a = func.plotInterval[0]
            if b <= func.plotInterval[1]:
                b = func.plotInterval[1]

        x = np.linspace(a, b, (b-a) * 10)
        for func in args:
            plt.plot(x, func.function(x))

        plt.grid()
        plt.show()
        return