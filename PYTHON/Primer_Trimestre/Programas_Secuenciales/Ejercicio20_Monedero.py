# Programa: Ejercicio20_Monedero.py
#
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y
# céntimos) después de pedirnos cuantas monedas tenemos de 2e, 1e, 50
# céntimos, 20 céntimos o 10 céntimos).
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 13/10/2019
#
#
# Variables a usar
#   * 10cnt <-- Variable para almacenar 10cnt
#   * 20cnt <-- Variable para almacenar 20cnt
#   * 50cnt <-- Variable para almacenar 50cnt
#   * 1eu   <-- Variable para almacenar 1 euro
#   * 2eu   <-- Variable para almacenar 2 euros
#   * total <-- Variable para almacenar 10cnt

# Algoritmo
# total = 10cnt * 0.1 + 20cnt * 0.2 + 50cnt * 0.5 + 1eu  + 2eu

# Entrada de datos
cnt10 = float(input("Introduza monedas de 10 centimos: "))
cnt20 = float(input("Introduza monedas de 20 centimos: "))
cnt50 = float(input("Introduza monedas de 50 centimos: "))
eu1   = float(input("Introduza monedas de 1 euro: "))
eu2   = float(input("Introduza monedas de 2 euros: "))


# Algoritmo

total = cnt10 * 0.1 + cnt20 * 0.2 + cnt50 * 0.5 + eu1 * 1  + eu2 * 2

# Salida de datos
print("El total es de:",total, " euros")
