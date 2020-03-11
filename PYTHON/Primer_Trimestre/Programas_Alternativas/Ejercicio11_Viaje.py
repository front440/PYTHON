# Programa: Ejercicio11_Viaje.py
#
# Proposito: El director de una escuela está organizando un viaje de
# estudios, y requiere determinar cuánto debe cobrar a cada alumno y
# cuánto debe pagar a la compañía de viajes por el servicio. La forma
# de cobrar es la siguiente: si son 100 alumnos o más, el costo por
# cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70
# euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la
# renta del autobús es de 4000 euros, sin importar el número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía
# de autobuses y lo que debe pagar cada alumno por el viaje.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * n     <-- numero de alumnos
  


# Leer datos
import math

print("Con este programa daremos con cuanto deberá de pagar cada alumno.")
print("-----------------------------------------------------------------")

n = float(input("¿Introduce el número de alumnos que iran de vije? "))
print("-----------------------------------------------------------------")

# Desarrollo

if n >= 100:
    print("El alumno le costara 65€")
elif n >= 50 or n <= 99:
    print("EL alumno tendrá que pagar 70€")
elif n >= 30 or n <= 49:
    print("EL alumno tendrá que pagar 95€")
if n < 30:
    print(f"el alumno tendrá que pagar {4000/n}€")
