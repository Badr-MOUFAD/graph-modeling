import numpy as np
import random

from ModalGraph import ModelGraph
from FunctionClass import Function

x = np.linspace(0, 10, 100)
y = np.cos(x)**2


f = ModelGraph(x, y)

g = f.modelWith([lambda t: 1, lambda t: np.cos(2*t)])

print(f.coefficientModel)
Function.plotFunctions(f.associatedFunction, g)
