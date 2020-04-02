# Programa: Ejercicio12_PideNumeroXeY.py
#
# Proposito: Pide al usuario dos pares de números x1,y2 y x2,y2, que
# representen dos puntos en el plano. Calcula y muestra la distancia
# entre ellos.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
#   * x1        <-- Coordenada asignada x1
#   * y1        <-- Coordenada asignada y1
#   -------------------------------
#   * x2        <-- Coordenada asignada x2
#   * y2        <-- Coordenada asignada y2
#   * distancia <-- distancia entre punto1 y punto2
#
# Algoritmo:
#   distancia = (1/2)**((x2 - x1)**2 + (y2 - y1)**2)

import math 

# Leer datos
print("---------------------------------------")
print("---------- Datos para punto 1 ---------")
x1 = float(input("introduce el valor para x1:"))
x2 = float(input("introduce el valor para x2:"))
print("---------------------------------------")
print("---------- Datos para punto 2 ---------")
y1 = float(input("introduce el valor para y1:"))
y2 = float(input("introduce el valor para 21:"))
print("---------------------------------------")

# Cáculo de datos
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
#distancia = math.sqrt(math.pow((x2 - x1),2)) + (math.pow((y2 - y1),2))

# Salida de datos
print("La distancia entre el punto 1 y el punto2 es: ", round(distancia, 2))
