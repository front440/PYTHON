# Programa: Ejercicio01_MayorOMenorque0.py
#
# Proposito: Realizar un algoritmo que pida números (se pedirá por
# teclado la cantidad de números a introducir). El programa debe
# informar de cuantos números introducidos son mayores que 0, menores
# que 0 e iguales a 0.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 24/10/2019
#
# Variables, algoritmos a usar
#   * contador  <-- Variable para almacenar contador de 1 a 10
#   * numero    <-- Variable para almacenar numero introducido

# Analisis, Algoritmos
# Deberemos de pedir una serie de números, de estos pedidos deberemos
# decir cuales son mayores, iguales o menores.
# Entonces, crearemos un contador hasta 5, para que pare en esta cifra
# y según nos vaya dando datos, iremos diciendo si es mayor, igual o menor
# mediante un "if". Cuando el contador llegue a 5, parará el programa.

# Leer datos


print("Este programa nos dirá que números de los introducidos son mayores, iguales o menores que 0.")
print("-----------------------------------------------------------------")

contador = 0

for contador in range(0,5):
    numero = int(input("Introduce el primer número: "))
    print(f"-Número {contador+1} introducido-")
    if numero < 0:
        print("Numero introducido menor que 0")
    elif numero == 0:
        print("Número igual a 0")
    else:
        print("Número mayor que cero")
    
print("Has llegado al límite para introducir datos")

    


