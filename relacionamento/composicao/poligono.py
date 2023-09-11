from relacionamento.composicao.lado import Lado
from relacionamento.composicao.triangulo import Triangulo


class Poligono:

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

    def adicionar_vertice(self, vertice):
        self.__vertices.append(vertice)

    def remover_vertice(self, vertice):
        self.__vertices.remove(vertice)

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

    def maior_lado(self):
        lado_maior = self.__lados[0]
        for lado in self.__lados:
            if lado.comprimento() > lado_maior.comprimento():
                lado_maior = lado
        return lado_maior

    def menor_lado(self):
        lado_menor = self.__lados[0]
        for lado in self.__lados:
            if lado.comprimento() < lado_menor.comprimento():
                lado_menor = lado
        return lado_menor

    def total_de_diagonais(self):
        return int((self.__total_de_vertices * (self.__total_de_vertices - 3)) / 2)

    def total_de_diagonais_partindo_de_um_vertice(self):
        return self.__total_de_vertices - 3

    def soma_dos_angulos_internos(self):
        return (self.__total_de_vertices - 2) * 180

    def classificacao(self):
        dic = {3: "Triângulo", 4: "Quadrilátero", 5: "Pentágono", 6: "Hexágono", 7: "Heptágono", 8: "Octógono",
               9: "Eneágono", 10: "Decágono", 11: "Undecágono", 12: "Dodecágono"}
        if self.__total_de_vertices < 13:
            return dic[self.__total_de_vertices]
        else:
            return "Polígono de {} lados".format(self.__total_de_vertices)

    def area_total(self):
        listas_de_vertices = []
        if self.total_de_diagonais_partindo_de_um_vertice() >= 1:
            for i in range(1, self.total_de_diagonais_partindo_de_um_vertice() + 2):
                lista = [self.__vertices[0], self.__vertices[i], self.__vertices[i + 1]]
                listas_de_vertices.append(lista)
        else:
            listas_de_vertices.append(self.__vertices)
        total = 0
        for lista in listas_de_vertices:
            triangulo = Triangulo(lista)
            total += triangulo.area()
        return total


from relacionamento.composicao.vertice import Vertice

vertices = []

numero_de_vertices = int(input("Informe o número de vértices: "))

if numero_de_vertices < 3:
    print('O número mínimo de vértices deve ser 3.')
    while numero_de_vertices < 3:
        numero_de_vertices = int(input("Informe o número de vértices: "))

for i in range(numero_de_vertices):
    coordenadas = input("Informe as coordenadas do vértice {}: ".format(i + 1))
    coordenadas = coordenadas.split(",")
    coordenada_x, coordenada_y = float(coordenadas[0]), float(coordenadas[1])
    vertice = Vertice(coordenada_x, coordenada_y)
    vertices.append(vertice)

p = Poligono(vertices)
for lado in p.lados:
    print(lado)
print(p.classificacao())
print(p.maior_lado())
print(p.menor_lado())
print(p.perimetro())
print(p.soma_dos_angulos_internos())
print(p.total_de_diagonais())
print(p.total_de_diagonais_partindo_de_um_vertice())
print(p.area_total())
