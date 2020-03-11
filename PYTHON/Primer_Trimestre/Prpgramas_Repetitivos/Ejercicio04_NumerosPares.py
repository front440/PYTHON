# Programa: Ejercicio04_NumerosPares.py
#
# Proposito: Escribir un programa que imprima todos los números pares
# entre dos números que se le pidan al usuario.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * letra  <-- Variable para almacenar letra introducida

# Analisis, Algoritmos
# Este programa deberá de pedir una letra. Nos dice que si el caracter
# introducido es un espacio, deberá de acabar el programa. En caso 
# contrario, el programa nos dirá sin es vocal o consonante.
# Implementaremos el operador while y el if.

# Leer datos


print("Este programa nos mostrará los numoers pares de un número introducido al otro número introducido.")
print("-----------------------------------------------------------------")

num1 = int(input("Introduce numero 1: ")) # Introducimos número 1
num2 = int(input("Introduce número 2: ")) # Introducimos número 2

if num1%2==1:
    num1+=1
for num in range(num1,num2,2):
    print(num)
