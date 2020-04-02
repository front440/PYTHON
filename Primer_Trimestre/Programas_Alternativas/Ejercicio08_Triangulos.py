# Programa: Ejercicio08_Triangulos.py
# Proposito: Programa que lea 3 datos de entrada A, B y C. Estos
# corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en
# cuenta los siguiente:
#
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables a usar
#   * lado1 <-- Almacenamos el valor de lado1
#   * lado2 <-- Almacenamos el valor de lado2
#   * lado3 <-- Almacenamos el valor de lado3
#
# Algoritmo:
# Triángulo rectángulo:
# Debe de cumplirse Pitagoras por lo que: a**2 = (b**2)+(c**2)
# Tiángulo equilatero:
# Todos los lados son iguales.
# Triángulo isósceles:
# Si dos lados son iguales
# Triángulo Escaleno:
# Si no se cumple niguna de las anteriores condiciones


import math

# Leer datos
print("Este programa nos dirá que tipo de triángulo es al introducir sus datos")
print("-----------------------------------------------------------------------")

lado1 = float(input("Ingresa el valor del lado 1: "))
lado2 = float(input("Ingresa el valor del lado 2: "))
lado3 = float(input("Ingresa el valor del lado 3: "))

# Desarrollo
if math.pow(lado1,2)+math.pow(lado2,2)==math.pow(lado3,2) or math.pow(lado1,2)+math.pow(lado3,2)==math.pow(lado2,2) or math.pow(lado3,2)+math.pow(lado2,2)==math.pow(lado1,2):
    print("Triángulo Rectángulo")
elif lado1 == lado2 == lado3:
    print("Tendremos un triángilo equilatero.")
elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado1 and lado2 != lado3) or (lado3 == lado1 and lado3 != lado2):
    print("El triágunlo sera isósceles")
else:
    print("El triángulo es escaleno")
