# Programa: Ejercicio11_Viaje.py
#
# Proposito: Realiza un programa que pida el día de la semana
# (del 1 al 7) y escriba el día correspondiente. Si introducimos otro
# número nos da un error.
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

if  n > 0 and n < 7:
    if n == 1:
        print("El número 1 le corresponde al Lunes")
    elif n == 2:
        print("El número 2 le corresponde al Martes")
    elif n == 3:
        print("El número 3 le corresponde al Miércoles")
    elif n == 4:
        print("El número 4 le corresponde al Jueves")
    elif n == 5:
        print("El número 5 le corresponde al Viernes")
    elif n == 6:
        print("El número 6 le corresponde al Sábado")
    elif n == 7:
        print("El número 7 le corresponde al Domingo")
else:
    print("EL número introducido es erroneo.")
    print("Reinicie el programa")
