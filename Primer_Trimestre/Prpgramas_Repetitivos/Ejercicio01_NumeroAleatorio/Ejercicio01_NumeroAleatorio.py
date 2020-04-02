# Programa: Ejercicio01_NumeroAleatorio.py
#
# Proposito: Crea una aplicación que permita adivinar un número.
# La aplicación genera un número aleatorio del 1 al 100. A continuación
# va pidiendo números y va respondiendo si el número a adivinar es
# mayor o menor que el introducido,a demás de los intentos que te
# quedan (tienes 10 intentos para acertarlo). El programa termina
# cuando se acierta el número (además te dice en cuantos intentos lo
# has acertado), si se llega al limite de intentos te muestra el número
# que había generado.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 24/10/2019
#
# Variables, algoritmos a usar
#   * i         <-- Variable para almacenar numero aleactorio de 0 a 100
#   * intentos  <-- Variable para almacenar contador de 1 a 10
#   * numero    <-- Variable para almacenar numero introducido

# Analisis, Algoritmos
# Deberemos de generar hacer generar un número del 0 a 100, para después
# tener que acertar con unos 10 intentos como máximo.

# Leer datos

import random

print("Este programa generará un número aleatoriamente para después tener que acertar.")
print("-----------------------------------------------------------------")

contador = 0
i = random.randint(0, 100)

for contador in range(1,11):
    numero = int(input("Introduce número: "))
    # print(f"{i}") Descomentar para ver número aleatorio
    if i == numero:
        print("Has acertado")
        break
    
    elif i < numero:
        print("El número introducido es mayor.")
        print(f"intento {intentos}")
        contador + 1
    elif i > numero:
        print("El número introducido es menor.")
        print(f"intento {intentos}")
        contador + 1
    elif contador == 10:
        print("Te has pasado de intentos")

    


