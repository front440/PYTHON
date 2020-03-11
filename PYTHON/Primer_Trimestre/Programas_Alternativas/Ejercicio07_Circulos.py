# Programa: Ejercicio07_Circulos.py
# Proposito: Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
#circunferencias y las clasifique en uno de estos estados:
#
# Exteriores
# Tangentes exteriores
# Secantes
# Tangentes interiores
# Interiores
# Concéntricas
#
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 16/10/2019
#
# Variables a usar
#   * x1 <-- valor para x1, circunferencia 1
#   * y1 <-- valor para 11, circunferencia 1
#   * y2 <-- valor para x1, circunferencia 2
#   * x2 <-- valor para x1, circunferencia 2
#   * distancia <-- Valor de la distancia entre centros
#
# Algoritmo, Casos:
#   Calcular distancia:
#   math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
#   Exteriores:
#   La distancia entre los centros, d, es mayor que la suma de los radios.
#   Las circunferencias no tienen puntos en común.
#
#   Secantes:
#   La distancia d es menor que la suma de los radios y mayor que su diferencia.
#   Tienen dos puntos en común.
#
#   Interiores:
#   La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios.
#   Una circunferencia está dentro de la otra, y por tanto no tienen puntos en común.
#
#   Tagentes Exteriores:
#   La distancia entre los centros es igual a la suma de los radios.
#   El centro de cada circunferencia es exterior a la otra y tienen un punto en común, punto de tangencia.
#
#   Tagentes Interiores:
#   La distancia entre los centros es igual a la diferencia entre los radios.
#   El centro de una de las circunferencias está dentro de la otra. Tienen un punto en común.
#
#   Concéntricas:
#   Tienen el mismo centro. La distancia d=0.
#   No tienen puntos en común, salvo que R=R', en este caso son la misma circunferencia.


# Leer datos
import math

print("Con este programa determinaremos que relación tienen dos circunferencias.")
print("-------------------------------------------------------------------------")

# Datos para la circunferencia 1
x1 = float(input("Posición de x1: "))
y1 = float(input("Posición de y1: "))
r1 = float(input("Radio de la primera circunferencia: "))

# Datos para la circunferencia 2
x2 = float(input("Posición de x2: "))
y2 = float(input("Posición de y2: "))
r2 = float(input("Radio de la segunda circunferencia: "))

# Cálculo
distancia = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
if distancia > (r1+r2):
    print("Estamos hablando de que la relación entre las circunferencia es Exterior.")
elif distancia < (r1+2) and  distancia >abs(r1-r2):
    print("Estamos hablando de que la relación entre las circunferencia es Exterior.")
elif distancia > 0 and distancia < abs(r1-r2):
    print("Estamos hablando de que la relación entre las circunferencia es Interior.")
elif distancia == (r1+r2):
    print("Estamos hablando de que la relación entre las circunferencia es Tangente Exterior.")
elif distancia == (r1-r2):
    print("Estamos hablando de que la relación entre las circunferencia es Tangente Interior.")
elif distancia == 0:
    print("Estamos hablando de que la relación entre las circunferencia es Concentrica")

