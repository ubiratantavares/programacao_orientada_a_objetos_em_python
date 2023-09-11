from datetime import datetime
from random import randint


class Pessoa:
    # atributo de classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    mes_atual = int(datetime.strftime(datetime.now(), '%m'))
    dia_atual = int(datetime.strftime(datetime.now(), '%d'))

    def __init__(self, nome, data_nascimento, peso, altura, comendo=False, falando=False):
        self.__id = Pessoa.gerar_id()
        self.__nome = nome  # atributo de instância
        self.__data_nascimento = data_nascimento
        self.__peso = peso
        self.__altura = altura
        self.__comendo = comendo
        self.__falando = falando

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def data_nascimento_date(self):
        return datetime.strptime(self.data_nascimento, '%d/%m/%Y').date()

    @property
    def ano_nascimento(self):
        return int(datetime.strftime(self.data_nascimento_date(), '%Y'))

    @property
    def mes_nascimento(self):
        return int(datetime.strftime(self.data_nascimento_date(), '%m'))

    @property
    def dia_nascimento(self):
        return int(datetime.strftime(self.data_nascimento_date(), '%d'))

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def comendo(self):
        return self.__comendo

    @property
    def falando(self):
        return self.__falando

    @property
    def idade(self):
        if Pessoa.ano_atual >= self.ano_nascimento:
            if Pessoa.mes_atual >= self.mes_nascimento:
                if Pessoa.dia >= self.dia_nascimento:
                    return Pessoa.ano_atual - self.ano_nascimento
        return Pessoa.ano_atual - self.ano_nascimento - 1

    def comer(self, alimento):
        if not self.__comendo and not self.__falando:
            self.__comendo = True
            print(f'{self.nome} está comendo {alimento}.')

    def falar(self, assunto):
        if not self.__comendo and not self.__falando:
            print(f'{self.nome} está falando sobre {assunto}.')
            self.__falando = True

    def parar_comer(self):
        if self.__comendo and not self.__falando:
            self.__comendo = False

    def parar_falar(self):
        if self.__falando and not self.__comendo:
            self.__falando = False

    def aumentar_altura(self, valor):
        self.altura += valor

    def diminuir_altura(self, valor):
        self.altura -= valor

    def aumentar_peso(self, peso):
        self.peso += peso

    def diminuir_peso(self, peso):
        self.peso -= peso

    def imc(self):
        return self.peso/self.altura**2

    # metodo de classe
    @classmethod
    def idade_por_ano_nascimento(cls, ano_nascimento):  # cls: refere-se a classe
        idade = cls.ano_atual - ano_nascimento
        return cls(idade)  # retorna a classe pessoa

    def classificar_peso(self):
        if self.imc() <= 18.5:
            return "Baixo peso"
        elif 18.5 < self.imc() <= 24.9:
            return "Peso Normal"
        elif 24.9 < self.imc() <= 29.9:
            return "Excesso de peso"
        elif 29.9 < self.imc() <= 34.9:
            return "Obesidade de classe I"
        elif 34.9 < self.imc() <= 39.9:
            return "Obesidade de classe II"
        else:
            return "Obesidade de classe III"

    # método estático
    @staticmethod
    def gerar_id():
        return randint(10_000, 19_999)

    def __str__(self):
        return "\nId: {}\nNome: {}\nData de Nascimento: {}\nPeso: {:.2f}\nAltura: {:.2f}\nIdade: {}\nClasse do IMC: {}\n"\
            .format(self.id, self.nome, self.data_nascimento, self.peso, self.altura, self.idade, self.classificar_peso())


from model.pessoa import Pessoa

pessoa = Pessoa('Ubiratan da Silva Tavares', "30/04/1973", 88.0, 1.73)

pessoa.comer('Maça')
pessoa.falar('POO')
pessoa.comer('Banana')
pessoa.parar_comer()
pessoa.falar('POO')
pessoa.comer("Banana")
pessoa.parar_falar()
print(pessoa)
