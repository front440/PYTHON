# Programa: Ejercicio10_Vinicultores.py
#
# Proposito: La asociación de vinicultores tiene como política fijar
# un precio inicial al kilo de uva, la cual se clasifica en tipos
# A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
# producto, ésta es de un solo tipo y tamaño, se requiere determinar
# cuánto recibirá un productor por la uva que entrega en un embarque,
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos
# al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
# tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de
# tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo
# para determinar la ganancia obtenida.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * kg    <-- Kilos que venden
#   * pb    <-- Precio base
#   * A1    <-- kg * (pb + (pb * 0.2))
#   * A2    <-- kg * (pb + (pb * 0.3))
#   * B1    <-- kg * (pb - (pb * 0.3))
#   * B2    <-- kg * (pb - (pb * 0.5))
#
  


# Leer datos
import math

print("Con este programa determinaremos la ganancia de la cosecha según el tipo de uva.")
print("--------------------------------------------------------------------------------")

pb = float(input("Cuál es el valor de la uva en kg/€: "))
kg = float(input("¿De cuantos Kilos quieres saber el precio de la uva?: "))

print("--------------------------------------------------------------------------------")

print("¿Que tipo de uva prefieres?")
# Menu
print("1) Uva tipo, A1: ")
print("2) Uva tipo, A2: ")
print("3) Uva tipo, B1: ")
print("4) Uva tipo, B2: ")
opcion = float(input("Pulsa el número que prefieras calcular: "))
print("--------------------------------------------------------------------------------")

# Algoritmo
a1 = kg * (pb + (pb * 0.2))
a2 = kg * (pb + (pb * 0.3))
b1 = kg * (pb - (pb * 0.3))
b2 = kg * (pb - (pb * 0.5))
# Desarrollo
if opcion == 1:
    print(f"la ganancia es de {a1}€")
elif opcion == 2:
    print(f"la ganancia es de {a2}€")
elif opcion == 3:
    print(f"la ganancia es de {b1}€")
elif opcion == 4:
    print(f"la ganancia es de {b2}€")
else:
    print("--------------------------------------------------------------------------------")
    print(f"Introduce un valor correcto")
    print(f"Reinicie el programa")
    
    
    
    
    
    
    
    
    
