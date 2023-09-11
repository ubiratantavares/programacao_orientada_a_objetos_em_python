from relacionamento.heranca.pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, nome, cpf, curso, dre, cr):
        Pessoa.__init__(self, nome, cpf)
        self.__curso = curso
        self.__dre = dre
        self.__cr = cr


if __name__ == "__main__":
    aluno1 = Aluno("José", "123457", "python", 5.0, 6.0)
    print(aluno1)

    aluno2 = Aluno("Maria", "123458", "Java", 6.0, 7.0)
    print(aluno2)
