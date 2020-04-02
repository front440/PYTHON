# Programa: Ejercicio05_Potencia.py
# Proposito: Realiza un algoritmo que calcule la potencia, para ello
# pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
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
#   * base      <-- Número que elevaremos a la potencia
#   * exponente <-- Número que utilizaremos como potencia
#
# Algoritmo:
# base**exponente   <-- cálculos positivos

import math

# Leer datos
print("Este programa nos dirá el resultado de elevar un número a la que queramos")
print("-------------------------------------------------------------------------")

base = float(input("Introduce número como base: "))
exponente = float(input("Introduce número como exponente: "))

# Cálculo
#resultado=base^exponente
#1/(base**abs(exponente))

if exponente > 0:
    print("El resultado de elevar",base,"a",exponente,f" es: {base**exponente}")
elif exponente == 0:
    print("El resultado de toda potencia a 0 es: 1")
elif exponente < 0:
    print(f"El resultado es: {1/(base**abs(exponente))}")
