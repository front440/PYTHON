# Programa: Ejercicio06_Filtro.py
# Proposito: Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el 
# mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a 
# dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe 
# imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
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
#   * nota <-- Almacenamos la nota
#   * edad <-- Almacenamos edad introducida
#   * sexo <-- Almacenamos, masculino o femenino
#
# Algoritmo:


# Leer datos
print("Este programa nos dirá que tipo de persona nos hará falta.")
print("----------------------------------------------------------")

nota = float(input("Introduce la nota: "))
edad = float(input("Introduce tu edad: "))
sexo = input("Introduce tu sexo (M/F): ")
#F = femenino
#M = masculino

# Cálculo

if nota >= 5:
    if edad >= 18:
        if sexo == 'F':
            print("Estás admitido")
        elif sexo == 'M':
            print("Eres un posible candidato")
else:
            print("No estás admitido")
