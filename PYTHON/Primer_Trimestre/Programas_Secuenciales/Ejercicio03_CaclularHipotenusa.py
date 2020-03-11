# Programa: Ejercicio3_CaclularHipotenusa.py
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
#
# Autor : Francisco Javier Campos
#
# Fecha: 09/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * hipotenusa (numérico) : Lado opuesto al ángulo recto en un triángulo rectángulo.
#   * cateto1 y cateto2: Lado que junto con otro forma el ángulo recto de un triángulo rectángulo.

#
# LEER 
# hipotenusa <-- math.sqrt(cateto1**2 + cateto2**2)

import math

# Petición de datos
try:
    cateto1 = float(input("Introduce el valor del cateto 1 "));
    cateto2 = float(input("Introduce el valor del cateto 2 "));

except:
    print("Debe de introducir datos numéricos")
    print("Ejecute el programa de nuevo introduciendo los datos correctamente.")
    exit(1);

# Cáculo
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Salida
print("La hipotenusa del triángulo rectángulo es", hipotenusa)

