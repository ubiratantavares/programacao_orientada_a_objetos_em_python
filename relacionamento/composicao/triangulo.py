from relacionamento.composicao.lado import Lado


class Triangulo:

    def __init__(self, vertices):
        self.__vertices = vertices
        self.__lados = self.__lista_de_lados()
        self.__total_de_vertices = len(self.__vertices)

    @property
    def vertices(self):
        return self.__vertices

    @property
    def lados(self):
        return self.__lados

    def __lista_de_lados(self):
        lados = []
        for i in range(0, len(self.__vertices)):
            if i < len(self.__vertices) - 1:
                lados.append(Lado(self.__vertices[i], self.__vertices[i+1]))
            else:
                lados.append(Lado(self.__vertices[i], self.__vertices[0]))
        return lados

    def perimetro(self):
        total = 0.0
        for lado in self.__lados:
            total += lado.comprimento()
        return total

    def area(self):
        sp = self.perimetro()/2
        a = sp
        for lado in self.lados:
            a *= (sp - lado.comprimento())
        return a**0.5
