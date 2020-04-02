# Programa: Ejercicio8_Sueldo
# Proposito: Un vendedor recibe un sueldo base mas un 10% extra por 
# comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá 
# por concepto de comisiones por las tres ventas que realiza en el mes y 
# el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
# sueldobase   <-- Sueldo sin comision del trabajador
# venta1      <-- Resultado de calcular el 10% de la venta
# venta2      <-- Resultado de calcular el 10% de la venta
# venta3      <-- Resultado de calcular el 10% de la venta
# sueldobruto <-- Sueldo bruto

# Algoritmo:
# venta1        <-- venta1 / 10 
# venta2        <-- venta2 / 10 
# venta3        <-- venta3 / 10 
# comision      <-- suma de valor1, valor2, valor3
# sueldoneto    <-- sueldobruto - comision

# Leer datos
sueldobase = float(input("Introduzca su sueldo base:"))
venta1 = float(input("Introduce valor venta 1: "))
venta2 = float(input("Introduce valor venta 2: "))
venta3 = float(input("Introduce valor venta 3: "))


# Cáculo de datos
venta1 = venta1 / 10
venta2 = venta2 / 10
venta3 = venta3 / 10
sueldobruto = sueldobase + venta1 + venta2 + venta3
comision = venta1 + venta2 + venta3


# Salida de datos
print("El trabajador recibira una comision de ", venta1,"€ por la primera venta")
print("El trabajador recibira una comision de ", venta2,"€ por la segunda venta")
print("El trabajador recibira una comision de ", venta3,"€ por la tercera venta")
print("----------------------------------------------------")
print("El trabajador recibira un sueldo base de: ", sueldobase, "y una comision de: ", comision)
print("En total se le abonará un sueldo de: ", sueldobruto)

