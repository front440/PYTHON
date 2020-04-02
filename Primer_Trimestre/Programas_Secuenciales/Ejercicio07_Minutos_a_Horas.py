# Programa: Ejercicio7_Minutos_a_Horas.py
# Proposito: Realiza un programa que reciba una cantidad de 
# minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
#   * horas <-- Calculará mediante una divion entera el numero de horas
#   * minutos <---  Calculará el reste de la division de las horas calculadas
#               de la division anterior
#
# Algoritmo:
# horas <-- horas // 60
# min   <-- - min % 60

# Leer datos
try:
    totalmin = float(input("Introduce el numero de minutos a calcular:"))
except:
    print("Los datos introducidos son incorrectos")
    print("Vuelve a ejecutar el programa")
    exit(1)

# Calculo de datos
horas = totalmin//60   # // quiere decir que la división será entera
minutos = totalmin%60  # % nos dara el resto de la división de horas // 60

# Salida de datos
print(totalmin,"Minutos son",horas, "horas y", minutos,"minutos:" )
