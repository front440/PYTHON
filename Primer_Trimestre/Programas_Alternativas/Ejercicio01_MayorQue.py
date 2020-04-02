# Programa: Ejercicio01_MayorQue.py
# Proposito: Algoritmo que pida dos números e indique si el primero es
# mayor que el segundo o no.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 16/10/2019
#
#
# Variables a usar
#   * a <-- Almacenaremos el primer numero
#   * b <-- Almacenaremos el segundo numero
#
# Algoritmo:
# a > b     <-- A es mayor
# a < b     <-- B es mayor
# a == b    <-- Iguales

# Leer datos
a = float(input("Inserta el primer número: "))
b = float(input("Inserta el segundo número: "))

# Algoritmo
if a > b:
    print("El primer número: ",a, ",es mayor") # Mostramos Cual es mayor
if a < b:
    print("El segundo número: ",b, ",es mayor")# Mostramos Cual es menor
elif a == b:
    print("Son iguales.") # En caso de que sean iguales, lo mostramos
