from relacionamento.heranca.veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, ano_fabricacao, modelo, marca, cilindradas, airbag):
        super().__init__(ano_fabricacao, modelo, marca)
        self.__cilindradas = cilindradas  # int
        self.__airbag = airbag  # booleano

    @property
    def cilindradas(self):
        return self.__cilindradas

    @property
    def airbag(self):
        return self.__airbag

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas

    @airbag.setter
    def airbag(self, airbag):
        self.__airbag = airbag

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.ano_fabricacao, self.modelo, self.marca, self.cilindradas, self.airbag)


from relacionamento.heranca.carro import Carro
v2 = Carro(2019, 'EcoSport', 'Ford', 16, True)
print(v2)
