from typing import Tuple

from Segundo_Trimestre.Poker_Dados.dado import Dado


class Jugador:

    def __init__(self, nombre):
        """
        Constructor de la clase
        :param nombre:
        """
        self.__nombre = nombre
        # Creamos los cinco dados necesarios para jugar al Poker de Dados y los almacenamos en una tupla
        self.__dado = (Dado(), Dado(), Dado(), Dado(), Dado())
        # Puntos totales.
        self.__puntos_totales = 0   # Inicializada a 0 cada vez que se crea un jugador
        self.__puntos_tirada = 0    #
        self.__tiro_premiado

        # Modificadores
        @property
        def nombre(self):
            return self.nombre

        @nombre.setter
        def nombre(self, value):
            self.nombre = value
