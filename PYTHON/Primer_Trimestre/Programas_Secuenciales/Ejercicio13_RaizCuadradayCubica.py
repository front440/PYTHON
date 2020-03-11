# Programa: Ejercicio13_RaizCuadradayCubica
# Proposito: Realizar un algoritmos que lea un número y que muestre 
# su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función 
# predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
#   * numero    <-- numero a exponer
#   * rcuadrada <-- raiz cuadrada de numero a exponer
#   * rcubica   <-- raiz cubica de numero a exponer
#
# Algoritmo:
# rcuadrada = numero ** (1/2)
# rcubica = numero ** (1/3)

# Leer datos
numero = float(input("Introduce número a exponer: "))

# Cálculo
rcuadrada = numero ** (1/2)
rcubica = numero ** (1/3)

# Salida
print("La raiz cuadrada de ", numero, "es", rcuadrada)
print("La raiz cubica de ", numero, "es", rcubica)
