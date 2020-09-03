import numpy as np
import random
import matplotlib.pyplot as plt

from FunctionClass import Function
from EuclidienSpace import EuclidienSpace


class ModelGraph:
    def __init__(self, X, Y):
        if len(X) != len(Y):
            raise Exception("list must have same lenght")

        self.plotInterval = [min(X), max(X)]
        self.associatedFunction = Function(function= ModelGraph.transformeToFunction(X, Y), plotInterval=self.plotInterval)
        self.__coefficientModel = []
        self.__error = None
        return

    @property
    def coefficientModel(self):
        return self.__coefficientModel

    @property
    def error(self):
        return self.__error

    def modelWith(self, modelFunctions):
        evn = EuclidienSpace(plotInterval=self.plotInterval)

        transModelFunctions = []
        for i in range(len(modelFunctions)):
            transModelFunctions.append(Function(function=modelFunctions[i], plotInterval=self.plotInterval))

        sev = evn.orthoNormalise(transModelFunctions)
        coordinateInSev = evn.getCoordinatesIn(self.associatedFunction, sev)

        #passing matrix : Pass(modelFunctions, sev base)
        passingMatrix = []
        for i in range(len(sev)):
            row = []
            for j in range(len(transModelFunctions)):
                row.append(evn.dotProduct(transModelFunctions[j], sev[i]))
            passingMatrix.append(row)

        passingMatrix = np.array(passingMatrix)
        passingMatrix = np.linalg.inv(passingMatrix)
        ##
        self.__coefficientModel = passingMatrix.dot(coordinateInSev)

        modelFunction = evn.projectOn(self.associatedFunction, sev)
        self.__error = evn.norm(modelFunction - self.associatedFunction)

        return modelFunction

    @staticmethod
    def transformeToFunction(X, Y):
        def func(x):
            try:
                for i in range(len(X) - 1):
                    if X[i] <= x and x <= X[i + 1]:
                        return (Y[i + 1] - Y[i]) / (X[i + 1] - X[i]) * (x - X[i]) + Y[i]

                raise Exception("Out of definition bounds")
            except: #case of x iterable
                return list(map(lambda t: func(t), x))

        return func