import random
import sys

# Creamos función para imprimir array
def mostrar_array(array):
    for i in array:
        print(i, end=" | ")


# generaArrayInt: Genera un array de tamaño n con números aleatorios
# cuyo intervalo (mínimo y máximo) se indica como parámetro.
def array2cadena(array):
    cadena = ""
    for i in array:
        cadena += str(i) + " | "
    return cadena

# generaArrayInt2: Genera un array de tamaño n con números aleatorios
# cuyo intervalo (mínimo y máximo) se indica como parámetro.
def genera_array_int(tamano, intervalo_min, intervalo_max):

    array = []

    for i in range(0,tamano):
        array.append(random.randint(intervalo_min, intervalo_max))

    return array


# minimoArrayInt: Devuelve el mínimo del array que se pasa como parámetro.
def minimo_array_int(array):
    minimo = sys.maxsize
    for i in array:
        if i < minimo:
            minimo = i

    return minimo # min(array)


# maximoArrayInt: Devuelve el máximo del array que se pasa como
# parámetro.
def maximo_array_int(array):
    maximo = -sys.maxsize
    for i in array:
        if i > maximo:
            maximo = i

    return maximo # max(array)

# mediaArrayInt: Devuelve la media del array que se pasa como parámetro.
def media_array_int(array):
    media = 0
    for i in array:
        media += i

    return media/len(array)


# estaEnArrayInt: Dice si un número está o no dentro de un array.
def esta_en_array_int(array, num):
    if num in array:
        return True
    else:
        return False


# posicionEnArray: Busca un número en un array y devuelve la posición
# (el índice) en la que se encuentra.
def posicion_en_array_int (array, num):
        posicion = array.index(num)
        return posicion


# volteaArrayInt: Le da la vuelta a un array.
def voltea_array_int(array):

    volteado = array.reverse()
    return volteado


# rotaDerechaArrayInt: Rota n posiciones a la derecha los números de un
# array.
def rota_derecha_array_int (array, n_rotar):
    copia = [None] * len(array)
    c = n_rotar
    for i in range(len(array)):
        copia[c] = array[i]
        c += 1
        if c == len(array):
            c = 0
    for i in range(len(array)):
        array[i] = copia[i]

# rotaIzquierdaArrayInt: Rota n posiciones a la izquierda los números de
# un array.
def rota_izquierda_array_int (array, n_rotar):
    copia = [None] * len(array)
    c = n_rotar
    for i in range(len(array),-1):
        copia[c] = array[i]
        c += 1
        if c == 0:
            c = len(array)
    for i in range(len(array)):
        array[i] = copia[i]



# Probamos las funciones
if __name__ == '__main__':
    # Generamos array aleatorio
    array = genera_array_int(10, 2, 15)

    # Imprimos array aleatorio por pantalla
    print("La función genera un array de números  aleatorios: ")
    mostrar_array(array)
    # print("La función genera un array de números  aleatorios:", array2cadena(array))

    print("")
    print("El valor mínimo del array generado es: ", minimo_array_int(array))

    print("El valor máximo del array generado es: ", maximo_array_int(array))

    print("La media del array es:", media_array_int(array))

    print("El número: ", esta_en_array_int(array, 10))

    print("El número que buscamos esta en la poscion: ", posicion_en_array_int(array, 10))

    voltea_array_int(array)
    print("El array volteado: ",array)

    rota_derecha_array_int(array, 3)
    print("El array rotado a la derecha: ", array)

    rota_izquierda_array_int(array, 1)
    print("El array rotado a la izquierda es: ", array)

