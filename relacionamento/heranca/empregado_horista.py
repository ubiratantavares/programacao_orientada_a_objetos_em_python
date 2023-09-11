from relacionamento.heranca.empregado import Empregado


class EmpregadoHorista(Empregado):

    def __init__(self, nome, cpf, rg, horas_trabalhadas, pagamento_por_hora):
        Empregado.__init__(self, nome, cpf, rg)
        self.horas_trabalhadas = horas_trabalhadas
        self.pagamento_por_hora = pagamento_por_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.pagamento_por_hora
