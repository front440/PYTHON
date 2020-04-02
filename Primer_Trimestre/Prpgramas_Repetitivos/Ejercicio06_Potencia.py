# Programa: Ejercicio06_Potencia.py
#
# Proposito: Escribe un programa que dados dos números, uno real
# (base) y un entero positivo (exponente), saque por pantalla el
# resultado de la potencia. No se puede utilizar el operador de potencia.
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * exponente  <-- Almacenamos el exponente
#   * base       <-- Alamcenamos base

# Analisis, Algoritmos
# Crearemos un algoritmo para resolver una potencia, para ello
# tendremos que dar con la sintaxis correcta, ya que podemos utilizar
# el operador de la potencia.
# El bucle en este caso, lo aplicaremos al exponente ya que no puede ser
# negativo y lo repetiremos hasta que se positivo.

# Leer datos

print("Este programa resolverá un algoritmo de una potencia.")
print("-----------------------------------------------------------------")

exponente = float(input("Introduce el exponente: "))
base = float(input("Introduce la base: "))

while exponente < 0:
    print("El exponente deberá de ser positivo: ")
    exponente = float(input("Introduce el exponente: "))

print(f"El resultado de la operación es {exponente**base}")
    
    
    

