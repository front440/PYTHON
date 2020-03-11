# Programa: Ejercicio14_NumeroInvertido.py
#
# Proposito: Dado un número de dos cifras, diseñe un algoritmo que 
# permita obtener el número invertido.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 11/10/2019
#
#
# Variables a usar
#   * numero    <-- Almacenamos el numero de 2 cifras
#   * invertido <-- Tratamos de coger el primer numero y el segundo y lo almacenamos
#   ---------------------------------------------------
#   * numero    <-- Almacenamos el numero de 2 cifras
#   * cifra1    <-- Almacenamos el primera cifra del numero introducido
#   * cifra2    <-- Almacenamos la segunda cifra del numero introducido
#   * invertido <-- Tratamos de coger el primer numero y el segundo y lo almacenamos
#
# Algoritmo:
#   invertido = (numero[1] + numero[0])
#   ---------------------------------------------------
#   i = i + 1
#   resto = numero % 10
#   numero = int(numero / 10)

# Entrada de datos
numero = input("Ingresa un número para cambiar orden: ")

# Calculamos datos
invertido = (numero[1] + numero[0])

# Salida de datos
print("El numero invertido es: ", invertido)

# Otra opcion
# numero = int(input("Ingresa un número para invertir: "))
# Calculos
# cifra1 = numero // 10
# cifra2 = numero % 10
# invertido = cifra2*10 + cifra1
# Muestramos resultado
# print("El número invertido es:, invertido")

# Otra opcion
# numero = input("Ingresa un número para cambiar orden: ")
# print("El numero invertido es", numero[::-1])
