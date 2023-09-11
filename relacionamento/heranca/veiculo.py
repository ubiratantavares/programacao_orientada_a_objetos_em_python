class Veiculo:

    def __init__(self, ano_fabricacao, modelo, marca):
        self.__ano_fabricacao = ano_fabricacao
        self.__modelo = modelo
        self.__marca = marca

    @property
    def ano_fabricacao(self):
        return self.__ano_fabricacao

    @property
    def modelo(self):
        return self.__modelo

    @property
    def marca(self):
        return self.__marca

    @ano_fabricacao.setter
    def ano_fabricacao(self, ano_fabricacao):
        self.__ano_fabricacao = ano_fabricacao

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def __str__(self):
        return '{}, {}, {}'.format(self.__ano_fabricacao, self.__modelo, self.__marca)


from relacionamento.heranca.veiculo import Veiculo

v1 = Veiculo(2019, 'EcoSport', 'Ford')
print(v1.marca)
print(v1.modelo)
print(v1)


