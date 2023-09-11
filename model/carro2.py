class Carro:

    def __init__(self, marca, modelo, ano, cor, combustivel, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.combustivel = combustivel
        self.velocidade = velocidade

    def acelerar(self):
        pass

    def freiar(self):
        pass

    def abastecer(self, quantidade):
        pass

    def sobe_marcha(self):
        pass

    def desce_marcha(self):
        pass

    def __str__(self):
      return "Marca: {}\nModelo: {}\nAno: {}\nCor: {}\nCombustivel: {}\nVelocidade: {}"\
        .format(self.marca, self.modelo, self.ano, self.cor, self.combustivel, self.velocidade)


carro1 = Carro("Ford", "Mustang GT Shelby", 2012, "Vermelho", 20, 180)
print(carro1)

carro2 = Carro("Chevrolet", "Camaro SS", 2012, "Amarelo", 23, 164)
print(carro2)
