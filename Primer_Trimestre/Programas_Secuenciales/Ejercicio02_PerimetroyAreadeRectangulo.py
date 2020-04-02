# Programa: Ejercicio2_PerimetroyAreadeRectangulo.py
# Calcula el perimetro y area de un rectángulo
#
# Autor : Francisco Javier Campos
#
# Fecha: 09/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * p : resultado de calcular perímetro --> (lado1+lado2)*2
#   * a : resultado de calcular area --> lado1*lado2
#
# LEER p
# perímetro <-- 2*PI*radio
# ESCRIBIR p
#
# LEER a
# area <-- lado1*lado2
# ESCRIBIR lado1 y lado2

# Petición de datos

lado1 = float(input("Introduce el valor del lado 1: "))
lado2 = float(input("Introduce el valor del lado 2: "))


# Cálculo
p = ((lado1 + lado2)* 2)
a = (lado1 * lado2)

print ("El perimetro del rectángulo es: ", p, "metros.")
print ("El area del rectángulo es: ", a, "metros cuadrados.")
    
exit


