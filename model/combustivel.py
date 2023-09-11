class Bomba:

    def __init__(self, tipo, valor_unitario, volume_do_tanque):
        self.__tipo = tipo
        self.__valor_unitario = valor_unitario
        self.__volume_do_tanque = volume_do_tanque

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor_unitario(self):
        return self.__valor_unitario

    @valor_unitario.setter
    def valor_unitario(self, valor):
        self.__valor_unitario = valor

    @property
    def volume_do_tanque(self):
        return self.__volume_do_tanque

    @volume_do_tanque.setter
    def volume_do_tanque(self, valor):
        self.__volume_do_tanque = valor

    def abastecer_por_valor_pago(self, valor_pago):
        quantidade_de_litros = valor_pago / self.valor_unitario
        if quantidade_de_litros <= self.volume_do_tanque:
            self.volume_do_tanque -= quantidade_de_litros
            print('O cliente abasteceu o veículo com {:.2f} litros, pagando R$ {:.2f}'
                  .format(quantidade_de_litros, valor_pago))
        else:
            print('Não há quantidade de litros suficiente para abastecimento do veiculo.')

    def abastecer_por_litro(self, quantidade_de_litros):
        if quantidade_de_litros <= self.volume_do_tanque:
            self.volume_do_tanque -= quantidade_de_litros
            valor_pago = quantidade_de_litros * self.valor_unitario
            print('O cliente abasteceu o veículo com {:.2f} litros, pagando R$ {:.2f}'
                  .format(quantidade_de_litros, valor_pago))
        else:
            print('Não há quantidade de litros suficiente para abastecimento do veiculo.')


bomba = Bomba("Gasolina", 5.35, 100.0)

bomba.abastecer_por_litro(50)

bomba.abastecer_por_valor_pago(50)

bomba.abastecer_por_valor_pago(100)
