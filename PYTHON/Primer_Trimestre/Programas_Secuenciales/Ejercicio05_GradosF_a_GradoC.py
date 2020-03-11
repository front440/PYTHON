# Programa: Ejercicio5_GradosF_a_GradoC.py
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#
# Autor : Francisco Javier Campos
#
# Fecha: 09/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * gradosf : Grados en unidad Fahrenheit
#   * gradosc : Grados en unidad Celsius

#
# LEER 
# gradosc <-- (gradosf - 32)* 5 / 9 

# Petición de datos
try:
    gradosf = float(input("Introuce un unidad en grados Fahrenheit: "))
except:
    print("Debe de introducir datos numéricos")
    print("Ejecute el programa de nuevo introduciendo los datos correctamente.")
    exit(1)
    
# Cálculo
gradosc = (gradosf - 32)* 5 / 9

# Salida de datos
print("El resultado de covertir ", gradosf, " Fahrenheit a grados celsius es: ",gradosc,"Celsius")
