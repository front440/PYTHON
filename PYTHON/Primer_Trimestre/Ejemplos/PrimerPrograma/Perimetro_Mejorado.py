# Programa: Perimetro_Mejorado.py
# Calcula el perimetro de una circunferencia y lo muestra
#
# Autor : Francisco Javier Campos
#
# Fecha: 09/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * radio(numérico): Radio de la circunferencia a tratar
#   * perímetro: almacenaré el perímetro --> 2*PI*radio
#
# LEER radio
# perímetro <-- 2*PI*radio
# ESCRIBIR perímetro
#

import math

# Petición de datos
try:
    radio = float(input("Dame el radio de la circunferencia "))
except:
    print("Tiene que introducir datos numéricos, lo introducido -", radio , "- no lo es.")
    print("Ejecunte el programa de nuevo introduciendo los datos correctamente.")
    exit(1)

# Cáculos
perimetro = 2*math.pi*radio

# Salida
print("El perímetro de la circunferencia es, ", perimetro)
