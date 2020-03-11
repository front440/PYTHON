# Programa: Ejercicio11_Viaje.py
#
# Proposito: Realiza un programa que pida por teclado el resultado
# (dato entero) obtenido al lanzar un dado de seis caras y muestre por
# pantalla el número en letras (dato cadena) de la cara opuesta al
# resultado obtenido.
#
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
# Ejemplo:
# Introduzca número del dado: 5
# En la cara opuesta está el "dos".
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * n     <-- numero introducido

# Leer datos
import math

print("Con este programa podremos saber el lado opuesto de la cara de un dado.")
print("-----------------------------------------------------------------")

n = float(input("¿El lado opuesto de que cara quieres saber? "))
print("-----------------------------------------------------------------")

# Desarrollo

if n == 1:
    print("El lado opuesto es 6")
elif n == 2:
    print("El lado opuesto es 5")
elif n == 3:
    print("El lado opuesto es 4")
elif n == 4:
    print("El lado opuesto es 3")
elif n == 5:
    print("El lado opuesto es 2")
elif n == 6:
    print("El lado opuesto es 1")
elif n <= 0 or n >= 6:
    print("EL número introducido es erroneo.")
    print("Reinicie el programa")
