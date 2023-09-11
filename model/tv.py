class TV:

    def __init__(self, canal=1, volume=1, ligada=False):
        self.__canal = canal
        self.__volume = volume
        self.__ligada = ligada

    def ligar(self):
        self.__ligada = True

    def desligar(self):
        self.__ligada = False

    def is_ligada(self):
        return self.__ligada

    def set_canal(self, canal):
        if canal >= 1:
            self.__canal = canal
        else:
            raise ValueError

    def get_canal(self):
        return self.__canal

    def set_volume(self, volume):
        if volume >= 1:
            self.__volume = volume
        else:
            raise ValueError

    def get_volume(self):
        return self.__volume

    def __str__(self):
        return """Canal: {}\nVolume: {}""".format(self.__canal, self.__volume)


tv = TV()

tv.ligar()
print(tv)

tv.set_canal(4)
tv.set_volume(50)
print(tv)
