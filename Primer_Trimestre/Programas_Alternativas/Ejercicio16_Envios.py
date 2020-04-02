# Programa: Ejercicio16_Envios.py
#
# Proposito: Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

# ZONA	UBICACIÓN	COSTO/GRAMO
# 1	América del Norte	24.00 euros
# 2	América Central	20.00 euros
# 3	América del Sur	21.00 euros
# 4	Europa	10.00 euros
# 5	Asia	18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.


#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * n     <-- numero introducido
#   * p     <-- precio introducido

# Leer datos


print("Este programa nos permite saber cual es el coste de un envio entre los diferentes paises.")
print("-----------------------------------------------------------------")

n = float(input("Introduce el peso del paquete (en gramos): "))
print("-----------------------------------------------------------------")

# Menu
print("1) America del Norte")
print("2) America Central")
print("3) America del Sur")
print("4) Europa")
print("5) Asia")

p = float(input("Introduce el pais al que quieras mandar el paquete: "))
print("-----------------------------------------------------------------")

# Desarrollo

if  n > 0 and n < 5000:
    if p == 1:
        print(f"El envio a America del Norte es {24*n}€") # Precio por gramo de 24€
    if p == 2:
        print(f"El envio a America Central es {20*n}€") # Precio por gramo de 20€
    if p == 3:
        print(f"El envio a America del Sur es {21*n}€") # # Precio por gramo de 21€
    if p == 4:
        print(f"El envio a Europa es {10*n}€") # Precio por gramo de 10€
    if p == 5:
        print(f"El envio a Asia es {18*n}€") # Precio por gramo de 18€
else:
    print("EL número introducido es erroneo.")
    print("Reinicie el programa")
