class Retangulo:

    def __init__(self, largura=1.0, altura=1.0):
        self.largura = largura
        self.altura = altura

    def get_largura(self):
        return self.largura

    def set_largura(self, largura):
        if largura > 0:
            self.largura = largura
        else:
            raise ValueError

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        if altura > 0:
            self.altura = altura
        else:
            raise ValueError

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


ret1 = Retangulo(1, 2)
print("Area: {:.2f}".format(ret1.area()))
print("Perimetro: {:.2f}".format(ret1.perimetro()))

ret2 = Retangulo()
print("Area: {:.2f}".format(ret2.area()))
print("Perimetro: {:.2f}".format(ret2.perimetro()))

try:
    ret2.set_altura(-1)
except ValueError:
    print("Valor não permitido para altura.")

try:
    ret2.set_largura(-10)
except ValueError:
    print("Valor não permitido para largura.")
