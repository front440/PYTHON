# Programa: Ejercicio11_Meses.py
#
# Proposito: Escribe un programa que pida un número entero entre uno
# y doce e imprima el número de días que tiene el mes correspondiente.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * n     <-- numero introducido

# Leer datos
import math

print("Con este programa podremos que número le corresponde a cada dia de la semana.")
print("-----------------------------------------------------------------")

n = float(input("Introduce el numero: "))
print("-----------------------------------------------------------------")

# Desarrollo

if  n > 0 and n < 12:
    if n == 1:
        print("Corresponde con Enero y tiene 31")
    elif n == 2:
        print("Corresponde con Febrero y tiene 28, menos los bisiestos que cuenta con 29")
    elif n == 3:
        print("Corresponde con Marzo y tiene 31")
    elif n == 4:
        print("Corresponde con Abril y tiene 30")
    elif n == 5:
        print("Corresponde con Mayo y tiene 31")
    elif n == 6:
        print("Corresponde con Junio y tiene 30")
    elif n == 7:
        print("Corresponde con Julio y tiene 31")
    elif n == 8:
        print("Corresponde con Agosto y tiene 31")
    elif n == 9:
        print("Corresponde con Septiembre y tiene 30")
    elif n == 10:
        print("Corresponde con Octubre y tiene 31")
    elif n == 11:
        print("Corresponde con Noviembre y tiene 30")
    elif n == 12:
        print("Corresponde con Diciembre y tiene 31")
else:
    print("EL número introducido es erroneo.")
    print("Reinicie el programa")
