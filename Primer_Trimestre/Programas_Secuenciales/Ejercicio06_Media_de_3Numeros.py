# Programa: Ejercicio6_Media_de_3Numeros.py
# Calcular la media de tres números pedidos por teclado.
#
# Autor : Francisco Javier Campos
#
# Fecha: 10/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * valor1 : leer valor1
#   * valor2 : leer valor2
#   * valor3 : leer valor3
#   * media : resultado de calcular los 3 valores
#
# LEER media
# media <-- (valor1 + valor2 + valor3) / 3
#

# Petición de datos
try:
    print("Calcular la media de tres números pedidos por teclado.")
    print("------------------------------------------------------")
    valor1 = float(input("Introduce primer valor: "))
    valor2 = float(input("Introduce segundo valor: "))
    valor3 = float(input("Introduce tercer valor: "))
    print("------------------------------------------------------")
except:
    print("El valor introducido no es válido")
    print("Vuelve a ejecutar el programa")
    exit(1)

# Cáculo
media = (valor1 + valor2 + valor3)/3

# Salida
print("El resultado de la media de calcular", valor1, valor2 ,"y", valor3,"es: ", media)
