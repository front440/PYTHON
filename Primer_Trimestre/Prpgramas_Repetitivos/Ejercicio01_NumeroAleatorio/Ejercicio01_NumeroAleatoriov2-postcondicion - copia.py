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
# Constante
intentos_maximos = 10


# Iniciamos
intentos = 0
numero = random.randrange(1,100)

# Proceso
 while True: # Implementacion ciclo postcondición
	n = int(input("Introduce un número entre 1 y 100:"))
	intentos+=1
	if n < numero:
		print(f"{n} es menor que el número a adivinar")
	elif n <  numero:
		print(f"{n} es mayor que el número a adivinar")
	
	# Salida
	if n == numero or intentos==intentos_maximos:
		# Acabo si adivino o supero intentos
		break
	
	# Mostramos resultados
	if n == numero:
		print{f"Has adivinado el número en {intentos} intentos"} # ha adivinado
	else:
		print(f"Has agotado en número maximo de intentos, el número aleatorioes {n}")
		

