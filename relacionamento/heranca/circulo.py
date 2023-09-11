from relacionamento.heranca.elipse import Elipse


class Circulo(Elipse):
    count = 0

    def __init__(self, raio):
        Elipse.__init__(self, raio, raio)
        Circulo.count += 1

    @property
    def raio(self):
        return self.__raioMaior

    @raio.setter
    def raio(self, raio):
        if raio > 0:
            self.__raioMaior = raio
            self.__raioMenor = raio
        else:
            raise ValueError

    @staticmethod
    def totalDeInstancias():
        return Circulo.count


if __name__ == "__main__":
    c1 = Circulo(5)
    print(c1.area())
    c2 = Circulo(8)
    print(c2.area())
    try:
        c3 = Circulo(-1)
    except ValueError:
        print("Valor inválido para o raio.")
    print(Circulo.totalDeInstancias())

