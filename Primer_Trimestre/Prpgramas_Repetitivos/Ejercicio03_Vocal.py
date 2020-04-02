# Programa: Ejercicio01_Vocal.py
#
# Proposito: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son
# vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando
# se introduce un espacio.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * letra  <-- Variable para almacenar letra introducida

# Analisis, Algoritmos
# Este programa deberá de pedir una letra. Nos dice que si el caracter
# introducido es un espacio, deberá de acabar el programa. En caso 
# contrario, el programa nos dirá sin es vocal o consonante.
# Implementaremos el operador while y el if.

# Leer datos


print("Este programa nos dirá si la letra introducida es vocal o consonante.")
print("El programa acabara con la entrada de un espacio")
print("-----------------------------------------------------------------")

letra = input("Introduce cualquier letra: ")
while letra != " ":
    if letra == "A" or letra == "a" or letra == "E" or letra == "e" or letra == "I" or letra == "i" or letra == "O" or letra == "o" or letra == "U" or letra == "u":
        print("la letra introducida es una vocal")
    else:
        print("La letra introducida es una consonante")
    letra = input("Introduce cualquier letra: ")
print("Ha terminado el programa.")
    





