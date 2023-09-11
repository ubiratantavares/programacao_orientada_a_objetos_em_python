class Conta:

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    # método privado - posso sacar?
    def _posso_sacar(self, valor):
        valor_total = self.saldo + self.limite
        return valor <= valor_total

    def sacar(self, valor):
        if self._posso_sacar(valor):
            self.__saldo -= valor
        else:
            raise ValueError

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def extratificar(self):
        print(self.__str__())

    # método de classe - método estático
    @staticmethod
    def codigo_do_banco(nome_banco):
        dic = {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
        return dic[nome_banco]

    def __str__(self):
        return "Titular: {}\nSaldo: {:.2f}\nLimite: {:.2f}\n".format(self.titular, self.saldo, self.limite)


from model.conta import Conta

c1 = Conta("Vitor", 1000, 5000)
c1.extratificar()

c1.depositar(1000)
c1.extratificar()

try:
    c1.sacar(500)
except ValueError:
    print("O valor solicitado para saque excedeu o saldo + limite disponível.")

c1.extratificar()

c1.limite = 1000
c1.extratificar()

c2 = Conta("Joao", 2500, 7000)
c2.extratificar()

c2.transferir(500, c1)
c2.extratificar()

c1.extratificar()

try:
    c1.sacar(5000)
except ValueError:
    print("O valor solicitado para saque excedeu o saldo + limite disponível.")

print(Conta.codigo_do_banco('BB'))
