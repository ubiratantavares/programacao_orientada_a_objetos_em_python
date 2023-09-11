class Carro:

    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0

    def imprimir(self):
        if self.velocidade == 0:
            print("{}, {}, {}.".format(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_maxima:
            print("{} {} indo a {} km/h.".format(self.modelo, self.cor, self.velocidade))
        else:
            print("{} {} indo muito rapido.".format(self.modelo, self.cor))

    def acelerar(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima
        self.imprimir()

    def parar(self):
        self.velocidade = 0
        self.imprimir()


carro1 = Carro("Brasília", 1968, 'Amarela', 80)
carro1.acelerar(40)
carro1.acelerar(80)
carro1.parar()

carro2 = Carro("Fuscão", 1981, "Preto", 95)
carro2.acelerar(50)
carro2.acelerar(100)
