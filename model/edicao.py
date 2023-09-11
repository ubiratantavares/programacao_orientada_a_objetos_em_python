class Edicao:

    def __init__(self, numero, volume, data, tiragem):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.tiragem = tiragem
        self.artigos = list()

    def verificar_quantidade_minima(self):
        if len(self.artigos) < 6:
            return True
        else:
            return False

    def verificar_quantidade_maxima(self):
        if len(self.artigos) <= 10:
            return True
        else:
            return False

    def adicionar_artigo(self, artigo):
        if self.verificar_quantidade_minima():
            self.artigos.append(artigo)
        elif self.verificar_quantidade_maxima():
            self.artigos.append(artigo)

    def listar_artigos(self):
        for artigo in self.artigos:
            print(artigo)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.numero, self.volume, self.data, self.tiragem)
