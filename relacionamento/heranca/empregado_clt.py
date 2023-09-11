from relacionamento.heranca.empregado import Empregado


class EmpregadoCLT(Empregado):

    def __init__(self, nome, cpf, rg, salario):
        Empregado.__init__(self, nome, cpf, rg)
        self.salario = salario

    def calcular_salario(self):
        return 13.3333333333 * self.salario
