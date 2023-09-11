import math


class Elipse:

    def __init__(self, raioMaior, raioMenor):
        if raioMaior > 0 and raioMenor > 0:
            self.__raioMaior = raioMaior
            self.__raioMenor = raioMenor
        else:
            raise ValueError

    @property
    def raioMaior(self):
        return self.__raioMaior

    @raioMaior.setter
    def raioMaior(self, raioMaior):
        if raioMaior > 0:
            self.__raioMaior = raioMaior
        else:
            raise ValueError

    @property
    def raioMenor(self):
        return self.__raioMenor

    @raioMenor.setter
    def raioMenor(self, raioMenor):
        if raioMenor > 0:
            self.__raioMenor = raioMenor
        else:
            raise ValueError

    def __str__(self):
        return "Raio maior: {}, Raio menor: {}".format(self.__raioMaior, self.__raioMenor)

    def area(self):
        return math.pi * self.__raioMaior * self.__raioMenor
