"""
Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también
pasamos como parámetro, de manera que:
    - Si el programa no recibe dos parámetros termina con un error 1.
    - Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
        antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
    - Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
        código 2.
    - Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje
        de error y código 2.
    - Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
"""
import string
import sys


def encripta_cesar(linea, desplazamiento):
    letras = string.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"
    cadena_encriptada = ""
    for caracter in linea:
        if caracter in letras:
            pos_donde_esta = letras.index(caracter)
            posicion_caracter_encriptado = (pos_donde_esta + desplazamiento) % len(letras)
            caracter_encriptado = letras[posicion_caracter_encriptado]
        else:
            caracter_encriptado = caracter
            # añadimos a la cadena encriptada
        cadena_encriptada += caracter_encriptado
    return cadena_encriptada


if __name__ == '__main__':

    # si el programa no recibe dos parámetros termina con error 1
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error al introducir los parámetros")
        exit(1)
    # Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee,
    # pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación que no se
    # haga.
    fichero_origen = sys.argv[1]
    if len(sys.argv) == 2:
        fichero_destino = fichero_origen
        while True:
            print("Esta operación machaca archivo de origen.")
            resp = input("Pulse S o N: ").upper()
            if resp == "S":
                break
            if resp == "N":
                print("WEBON")
                exit(1)
    else:
        fichero_destino = sys.argv[2]

    # Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
    # código 2.
    try:
        fichero = open(fichero_origen, "r")
    except FileNotFoundError:
        print("No se ha podido abrir el fichero")
        exit(2)



    # Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
    while True:
        try:
            desplazamiento = int(input("Introduce el número de desplazamientos para la encriptación: "))
        except ValueError:
            print("Introduce número entero.")
        else:
            break

    origen = fichero.readlines()
    fichero.close()

    #Abre y escribe el fichero.
    try:
        fichero = open(fichero_destino, "w")
    except PermissionError or FileNotFoundError:
        print("No se puede  escribir el fichero.")
        exit(2)

    for linea in origen:
        fichero.write(encripta_cesar(linea, desplazamiento))
    fichero.close()
