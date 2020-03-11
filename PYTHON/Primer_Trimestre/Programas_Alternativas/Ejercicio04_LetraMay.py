# Programa: Ejercicio04_LetraMay.py
# Proposito: Programa que lea una cadena por teclado y compruebe si
# es una letra mayúscula.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 16/10/2019
#
# Variables a usar
#   * letra     <-- Almacenamos la letra
#
# Algoritmo:
# letra.upper() <-- operando que nos muestra si es mays o mins

# Leer datos
print("Con este programa sabremos si una letra es mayúscula")
print("-----------------------------------------------------")

letra = input("Introduce la letra: ")

# Cálculo
if letra.upper():
    print("Está escrito en mayusculas") # Salida de datos verdadera
else:
    print("No está escrito en mayusculas") # Salida de datos falsa
