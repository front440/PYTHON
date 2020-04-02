from Segundo_Trimestre.Poker_Dados.dado import Dado
from Segundo_Trimestre.Poker_Dados.jugador import Jugador

import os


class Poker_dados:


def __init__(self):
    __jugadores = list()

@property
def jugadores(self, value):
    self.__jugadores = value

@jugadores.setter
def jugadores(self, value):
    self.jugadores = value

def pedir_jugadores():
    print("Introduce el número de jugadores de la partidad")
    while True:
        try:
            # Introducimos el número de jugadores, sabiendo que el máximo será 5
            numero_jugadores = int(input("Introduce el número de jugadores: "))

            if numero_jugadores <= 5:
                alta_jugadores()

            else:
                print("introduce un número de jugadores correcto")

        except ValueError:
            print("introduce un número de jugadores correcto")


def ayuda():
    """
    Muestra por pantalla la ayuda del juego
    :return:
    """
    print(
        "\n\n"
        "-------------------------------------------------------------------------------------------------------"
        "\nAYUDA DEL JUEGO\n"
                
        "1.Introducción \n"
        "Tiempo de juego: alrededor de cinco minutos por vuelta.\n"
        "Número de jugadores: sin límite. Pero es mejor cuando se juega de a cinco o menos.\n"
        "Número de dados: cinco.\n"
        "Elementos: un cubilete.\n"
        "Es esencialmente un juego de cartas que en lugar de estas, emplea dados. Como su equivalente en\n"
        "los naipes, el poker se juega por dinero, pero el procedimiento para las apuestas no es el mismo.\n\n"

        "2.Objetivo\n"
        "Hacer el 'juego de Poker' de mayor valor.\n\n"

        "3.Comienzo \n"
        "Cada jugador tira dos veces por turno. si esta satisfecho con el resultado, se puede plantar\n"
        "después del primer tiro. Luego anota el valor de su jugada y pasa los dados al de su izquierda o \n"
        "puede también apartar los dados que desee de su primer tiro y hacer con los restantes su segundo y\n"
        "último tiro. Una vez que se ha apartado un dado no se lo debe volver a arrojar. Después del segundo\n"
        "intento, el jugador anota el valor de su jugada y pasa los dados al de su izquierda.\n"

        "El participante que haya hecho el juego de mayor valor gana el pozo.\n"

        "Los juegos se clasifican en orden descendente de la siguiente forma:\n\n"

        "1. poker real (cinco iguales)\n"
        "2. poker cuádruple (cuatro iguales)\n"
        "3. full (tres iguales y un par)\n"
        "4. escalera mayor 2-3-4-5-6\n"
        "5. escalera menor 1-2-3-4-5\n"
        "6. piernas (triples)\n"
        "7. pares dobles\n"
        "8. pares.\n\n"

        "La jugada que no contenga por lo menos un par, no tiene valor.\n\n"
        "Si dos o más jugadores hacen un juego de igual valor, gana el que tenga el puntaje mas alto .Así\n"
        "cuatro 4 valen mas que cuatro 3.\n\n"
        "En el poker el as es el valor mas alto y por lo tanto los números se clasifican (en orden "
        "descendente) de la siguiente manera: 1-6-5-4-3-2-.\n\n"
        "Si dos o más participantes hacen un mismo juego con dados de igual valor, jugaran nuevamente para\n"
        "determinar el resultado. Los valores de los dados que no hacen al juego no se consideran para desempatar\n\n"
        "Así , si un jugador saca cuatro 4 y un 6, y otro saca cuatro y un 3 , se considera empate y la\n"
        "segunda vuelta de juego entre ambos determinará al ganador\n\n"
        "Cuando se juega entre dos personas, por lo general quien gana tres vueltas de las cinco se queda\n"
        "con el pozo."
        "\n\n"
        "-------------------------------------------------------------------------------------------------------")


def borra_pantalla():
    """"
    Este método detectará el S.O. del equipo y borra la pantalla
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def salir():
    """
    Sale del programa
    :return:
    """
    print("Hasta la próxima!")
    exit(1)


def empezar_partida():
    """
    Empieza la partida del poker
    :return:
    """
    print("Empieza la partida")
    pedir_jugadores()


if __name__ == '__main__':

    while True:
        try:
            print("BIENVENIDO AL JUEGO DE POKER DE DADOS.")
            print("1) Ayuda del juego.")
            print("2) Jugar.")
            print("3) Salir.")
            opcion = int(input("Introduce una opción: "))

            if opcion == 1:
                borra_pantalla()
                ayuda()

            elif opcion == 2:
                borra_pantalla()
                empezar_partida()

            elif opcion == 3:
                borra_pantalla()
                salir()

            else:
            print("Introduce una opción valida: ")

        except ValueError:
        print("Introduce una opción valida: ")
