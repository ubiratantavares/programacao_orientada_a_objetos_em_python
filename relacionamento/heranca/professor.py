from relacionamento.heranca.pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome, cpf, formacao, siape):
        Pessoa.__init__(self, nome, cpf)
        self.__formacao = formacao
        self.__siape = siape


if __name__ == "__main__":
    professor1 = Professor("Francisco", "123478", "Sistemas de Computação", 1357)
    print(professor1)
