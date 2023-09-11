class Lado:

    def __init__(self, vertice1, vertice2):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2

    @property
    def vertice1(self):
        return self.__vertice1

    @property
    def vertice2(self):
        return self.__vertice2

    def comprimento(self):
        return ((self.vertice2.x - self.vertice1.x)**2 + (self.vertice2.y - self.vertice1.y)**2)**0.5

    def __str__(self):
        return "{:.1f}".format(self.comprimento())
