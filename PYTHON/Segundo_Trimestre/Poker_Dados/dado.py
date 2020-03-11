import random

"""
Clase dado:
    Simularemos el comportamiento de un dado, lo crearemos adaptado para jugar
    al poker. Para ello guardamos lo los valores de las caras en una tupla.
"""


class Dado:

    def __init__(self):
        self.__valores = ("Negro", "Rojo", "J", "Q", "K", "As")
        self.__valor = random.choice(self.__valores)


    def valores(self):
        return self.__valores

    # Modificadores
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value


    def tirada(self):
        """
        Simula la tirada del dado.
        :return: valor del dado.
        """
        self.valor = random.choice(self.__valores)
        return self.valor


if __name__ == "__main__":
    d = Dado()
    print("Caras del dado:", d.valor)
    print("Tiramos los dados una vez: ", end="")
    for i in range(5):
        d.tirada()
        print(d.valor, end=" ")
