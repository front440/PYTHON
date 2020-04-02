# Programa: Ejercicio09_AñoBisiesto.py
# Proposito: Escribir un programa que lea un año indicar si es
# bisiesto. Nota: un año es bisiesto si es un número divisible por
# 4, pero no si es divisible por 100, excepto que también sea divisible
# por 400.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 17/10/2019
#
# Variables a usar
#   * nota <-- Almacenamos la nota
#   * edad <-- Almacenamos edad introducida
#   * sexo <-- Almacenamos, masculino o femenino
#
# Algoritmo:
# Para que un año sea bisiesto y lo mostremos este deberá de ser 
# divisible entre 4 y entre 400. Utilizaremos los objetos booleanos


# Leer datos

print("Este programa nos dirá si un año es bisiesto o no.")
print("----------------------------------------------------------")

año = float(input("Introduce el año bisiesto: "))

# Cálculo

if año % 4 and año % 400:
    print(f"El año {año} no es bisiesto") # Salida falsa
else:
    print(f"El año {año} es bisiesto") # Salida verdadera
