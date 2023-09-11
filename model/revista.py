class Revista:

    def __init__(self, titulo, issn, periodo):
        self.titulo = titulo
        self.issn = issn
        self.periodo = periodo
        self.edicoes = list()

    def adicionar_edicao(self, edicao):
        self.edicoes.append(edicao)

    def remove_edicao(self, edicao):
        self.edicoes.remove(edicao)

    def listar_edicoes(self):
        for edicao in self.edicoes:
            print(edicao)

    def __str__(self):
        return "{}, {}, {}".format(self.titulo, self.issn, self.periodo)