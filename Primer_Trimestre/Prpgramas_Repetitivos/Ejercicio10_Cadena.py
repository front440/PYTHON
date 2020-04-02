# Programa: Ejercicio10_Cadena.py
#
# Proposito: Pide una cadena y un carácter por teclado y muestra
# cuantas veces aparece el carácter en la cadena
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * cadena    <-- Almacenamos la cadena que introduciremos
#   * caracter  <-- Almacenamos el caracter que queremos contar
#   * contador  <-- Almacenamos el número de veces que aparece el caracter

# Analisis, Algoritmos
# Este programa contará el número de veces que aparece el caracter en 
# una cadena. Para ello emplearemos el ciclo for.

# Leer datos

print("Este programa nos permitira contabilizar el tiempo como lo haría un cronometro.")
print("-----------------------------------------------------------------")

cadena = str(input("Introduce una cadena: "))
caracter = str(input("Introduce un caracter: "))
contador = 0

# Calculos

for i in cadena:
    if i == caracter:
        contador +=1

print(f"El caracter introducido es {caracter} y aparece {contador} veces")
