from relacionamento.heranca.empregado import Empregado


class PrestadorDeServico(Empregado):

    def __init__(self, nome, cpf, rg, pagamento_avulso):
        Empregado.__init__(self, nome, cpf, rg)
        self.pagamento_avulso = pagamento_avulso

    def calcular_salario(self):
        return self.pagamento_avulso
    