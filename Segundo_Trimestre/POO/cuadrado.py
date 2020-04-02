from Segundo_Trimestre.rectangulo import rectangulov3

class Cuadrado(Rectangulo):
    """
    Implementamos la clase Cuadrado partiendo de la clase Rectángulo.
    Consideraremos que un cuadrado es un rectángulo con base==altura
    """
    def __init__(self,lado):
        super(Cuadrado, self).__init__(lado, lado)

    @property
    def lado(self):
        return self.__base

    @lado.setter
    def lado(self, value):
        self.__base = value
        self.altura = value