# Programa: Ejercicio15_IntercambiarVariables.py
#
# Proposito: Dadas dos variables numéricas A y B, que el usuario 
# debe teclear, se pide realizar un algoritmo que intercambie los
# valores de ambas variables y muestre cuanto valen al final las dos variables.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 11/10/2019
#
#
# Variables a usar
#   * a     <-- Asignación A
#   * b     <-- Asignación B
#   * aux   <-- Guardará el valor de A
#           La variable de aux es utilizada para no peder el valor de la
#           varaible a, ya que si no lo hiciesemos de esta manera se perderia.
#
# Algoritmo:
# aux = a
# a = b
# b = aux

# Entrada de datos

a = float(input("Introduce valor para A: "))
b = float(input("Introduce valor para B: "))
print("-----------------------------------")

# Cálculo

aux = a
a = b
b = aux 


# Salida de datos
print("-----------------------------------")
print("A es igual a: " ,a )
print("B es igual a: ", b)
print("-----------------------------------")

# Otra forma
# a = 1
# b = 2
# a,b = b,a #

