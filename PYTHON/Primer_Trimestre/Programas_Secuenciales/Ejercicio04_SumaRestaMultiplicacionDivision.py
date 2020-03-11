# Programa: Ejercicio4_SumaRestaMultiplicacionDivision.py
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
#
# Autor : Francisco Javier Campos
#
# Fecha: 09/10/2019
#
# Alogoritmo
#
# Variables a usar:
#   * valor1
#   * valor2

#
# LEER 
# Suma <-- valor1 + valor2
# Resta <-- valor1 - valor2
# Multiplicación <-- valor1 * valor2
# División <--- valor1 / valor2

# Petición de datos

try:
    valor1 = float(input("Introduce el valor de valor1 "))
    valor2 = float(input("Introduce el valor de valor2 "))

except:
    print("Debe de introducir datos numéricos")
    print("Ejecute el programa de nuevo introduciendo los datos correctamente.")
    exit(1)

# Cálculo
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2

# Salida de datos
print("El resultado de la suma de", valor1, " y ", valor2, "es", suma)
print("El resultado de la resta de", valor1, " y ", valor2, "es", resta)
print("El resultado de la multiplicación de", valor1, " y ", valor2, "es", multiplicacion)
print("El resultado de la division de", valor1, " y ", valor2, "es", division)
