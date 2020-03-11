import pickle

if __name__ == '__main__':
    cadena1 = 'Puedes comerme los huevos'
    cadena2 = 'Oh yes'

    archivo = open('fichero2.txt', 'w')
    archivo.write(cadena1 + "\n")
    archivo.write(cadena2 + "\n")
    archivo.close()

    archivo = open('fichero2.txt', 'r')
    while True:
        linea = archivo.readline()
        if not linea:
            break
        print(linea)
    archivo.close()

    lista = [1, 2, 3, 4, 5, 6]
    lista2 = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    archivo = open('fichero3.txt', 'w')
    archivo.writelines(lista2)
    archivo.close()

    archivo = open('fichero3.txt', 'r')
    while True:
        linea = archivo.readline()
        if not linea:
            break
        print(f"{linea}")
    archivo.close()

    # Declara lista
    lista = ['Perl', 'Python', 'Ruby']

    # Abre archivo binario para escribir
    archivo = open('lenguajes.dat', 'wb')

    # Escribe lista en archivo
    pickle.dump(lista, archivo)

    # Cierra archivo
    archivo.close()

    # Borra de memoria la lista
    del lista

    # Abre archivo binario para leer
    archivo = open('lenguajes.dat', 'rb')

    # carga lista desde archivo
    lista = pickle.load(archivo)

    # Muestra lista
    print(lista)

    # Cierra archivo
    archivo.close()
