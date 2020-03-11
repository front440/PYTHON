# Programa: Ejercicio07_Cuota.py
#
# Proposito: Una persona adquirió un producto para pagar en 20 meses.
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así
# sucesivamente. Realizar un programa para determinar cuánto debe pagar
# mensualmente y el total de lo que pagará después de los 20 meses.
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * cuota_1   <-- Almacenamos el valor de la cuota 1, que es 10€
#   * cuota     <-- Almacenamos el valor total de la cuota

# Analisis, Algoritmos
# Crearemos un algoritmo que mediante el for in range, hasta la suma
# de 20 meses vayamos multiplicando, el valor de la cuota por 2 cada
# vez.

# Leer datos

print("Este programa nos permitirá calcular la cuota de 20 meses.")
print("-----------------------------------------------------------------")
cuota = 10
cuota_1 = 0

for cuota in range(0,21):
    cuota_1 = cuota_1 + cuota
    cuota *= 20
    print(f"La cuota será {cuota}")
    
    
    

