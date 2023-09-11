class Pessoa:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def __str__(self):
        return "{}, {}".format(self.__nome, self.__cpf)


if __name__ == "__main__":
    pessoa = Pessoa("João", "123456")
    print(pessoa)