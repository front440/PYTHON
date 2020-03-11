# Programa: Ejercicio08_Cronometro.py
#
# Proposito: Hacer un programa que muestre un cronometro, indicando las
# horas, minutos y segundos.
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * horas     <-- Almacenamos horas
#   * minutos   <-- Almacenamos minutos
#   * segundos  <-- Almacenamos segundos

# Analisis, Algoritmos
# Este programa será igual que un cronometro, para ello importaremos
# time, y crearemos 3 for in para cada uno ellos. Necesitaremos un
# contador de segundos, que lo usaremos con la clase time.sleep.

# Leer datos
import time

print("Este programa nos permitira contabilizar el tiempo como lo haría un cronometro.")
print("-----------------------------------------------------------------")

print("Iniciamos el cronometro.")

for horas in range(0,24): 
    for minutos in range(0,60):
        for segundos in range(0,60):
            print(f"{horas} horas,{minutos} minutos y {segundos} segundos")
            time.sleep(1)
    
    

