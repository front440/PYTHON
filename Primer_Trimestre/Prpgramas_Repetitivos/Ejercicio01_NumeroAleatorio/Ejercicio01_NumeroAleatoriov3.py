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
intentos = 10
numero = random.randrange(1,100)

# Proceso

# Implementamos un ciclo postcondicion, ejecutamos la instruccion
# antes de entrar en el ciclo y al final del ciclo.
n = int(input("Introduce un número entre 1 y 100:"))

# Proceso
intentos = intentos_maximos-1
while n != numero and intentos>0:
	
	if n < numero:
		print(f"{n} es menor que el número a adivinar")
	elif n <  numero:
		print(f"{n} es mayor que el número a adivinar")
		intentos -=1
	n = int(input("Te quedan "+ str(intentos) + ". Introduce un número entre 1 y 100:"))
	
	
	# Salida
	if numero == n:
		print(f"Has adivinado el numero en {intentos} intentos")
		# Acabo si adivino o supero intentos
	else:
		print(f"Has agotado  el número maximo de intentos. El número a adivinar era {numero}")
	
	# Mostramos resultados
	if n == numero: # ha adivinado
		print(f"Has adivinado el número en {intentos} intentos") # ha adivinado
	else:
		print(f"Has agotado en número maximo de intentos, el número aleatorioes {n}")
		

