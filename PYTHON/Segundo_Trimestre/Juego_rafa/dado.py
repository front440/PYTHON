import random


class Dado:
    """
    Esta clase simula el comportamiento de un dado.
    """
    def __init__(self, *valores):
        """
        Crea el objeto que simula un dado.
        :param valores: tupla (no es una lista) de valores de las caras del dado.
        """
        self.__caras = valores
        self.__cara = random.choice(valores)

    @property
    def cara(self):
        """
        Similar getter de Java, pero con una filosofía 'pythonica'.
        En Python se prefiere acceder a los atributos directamente, si son ocultos se hace con una propiedad.
        """
        return self.__cara

    @property
    def caras(self):
        """
        Similar getter de Java, pero con una filosofía 'pythonica'.
        En Python se prefiere acceder a los atributos directamente, si son ocultos se hace con una propiedad.
        """
        return self.__caras

    def tirada(self):
        """
        Simula la tirada del dado.
        :return: valor del dado.
        """
        self.__cara = random.choice(self.__caras)
        return self.__cara


if __name__ == "__main__":
    d = Dado("As","K","Q","J","6","5")
    print("Caras del dado:", d.caras)
    print("Tiramos dado 5 veces: ", end="")
    for i in range(5):
        d.tirada()
        print(d.cara, end=" ")
    print("\nTiramos dado 5 veces: ", end="")
    for i in range(5):
        print(d.tirada(), end=" ")