# Programa: Ejercicio11_DistanciaEntreNumeros.py
#
# Proposito: Pide al usuario dos números y muestra la "distancia" 
# entre ellos (el valor absoluto de su diferencia, de modo que el 
# resultado sea siempre positivo).
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
# numero1 <-- valor del numero 1
# numero2 <-- valor del numero 2
# diferencia <-- Resultado de restar numero1 y numero2

# Algoritmo:
# diferencia <-- numero1 - numero2

import math

# Entrada de datos
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Cálculo
diferencia = numero1 - numero2

# Salida de datos
print("La diferencia de números entre ", numero1 ,"y ", numero2, " es:", abs(diferencia)) # abs covierte cualquier valor o variable de negativa a positiva

