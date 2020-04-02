# Programa: Ejercicio03_Division.py
# Proposito: Crea un programa que pida al usuario dos números y muestre su división
# si el segundo no es cero, o un mensaje de aviso en caso
# contrario.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 16/10/2019
#
# Variables a usar
#   * diviendo  <-- Número a dividir
#   * dividor   <-- Número con el que dividiremos
#   * Resultado <-- Almacenamos resultado de la division
#
# Algoritmo:
# divisor == 0 or dividiendo == 0 <-- error
# diviendo / divisor = resultado

# Leer datos
print("Con este programa dividiremos los número introducidos")
print("-----------------------------------------------------")

dividiendo = float(input("Introduce que número a dividir: "))
divisor = float(input("Introduce numero con el que dividiremos: "))

# Cálculo
if divisor == 0:
    print("Número introducido es erroneo")
    print("Vuelve a ejecutar el programa con un númer correcto")
else:
    print(f"El resultado de la operación es: {dividiendo/divisor}")

