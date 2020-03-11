# Programa: DescuentoCompra.py
#
# Proposito: Una tienda ofrece un descuento del 15% sobre el total de 
# la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
# valorcompra       <-- total de la compra
# preciodescuento   <-- precio con descuento

# Algoritmo:
# preciodescuento   <-- valorcompra - 0.15

# Leer datos

valorcompra = float(input("Introduce el valor de la compra: "))


# Cáculo de datos
preciodescuento = valorcompra + (valorcompra * 0.15)

# Salida de datos
print("El valor de la compra sin descuento es", preciodescuento)
