# Programa: Ejercicio2_NumeroPar.py
# Proposito: Escribe un programa que lea un número e indique
# si es par o impar..
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 16/10/2019
#
#
# Variables a usar
#   * n <--- Número introducido
#
# Algoritmo:
# n % 2  

# Leer datos
print("En este ejercicio os mostraremos si el número es par o impar.")
print("-------------------------------------------------------------")
n = float(input("Introduce número: "))
print("-------------------------------------------------------------")

# Cálculo
if n % 2:
    print("El número introducido es impar") #Imprimimos resultado falso
else:
    print("El número introducido es par") #Imprimimos resultado verdadero    

