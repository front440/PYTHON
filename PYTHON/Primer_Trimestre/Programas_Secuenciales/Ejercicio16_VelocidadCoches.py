# Programa: Ejercicio16_Ciclista.py
#
# Proposito: Un ciclista parte de una ciudad A a las HH horas, 
# MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra
# ciudad B es de T segundos. Escribir un algoritmo que determine
#  la hora de llegada a la ciudad B.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 11/10/2019
#
#
# Variables a usar
#   * hs          <-- Hora de salida
#   * ms          <-- Minuto de salida
#   * ss          <-- Segundo de salida
#   * tiempos    <-- hora de salida en segundos
###################################################
#   * tt          <-- Tiempo que se tarda en llegar a la ciudad
#   * mt          <-- Tiempo que se tarda en llegar a la ciudad
#   * st          <-- Tiempo que se tarda en llegar a la ciudad
###################################################
#   * hf          <-- Hora final
#   * mf          <-- minutos finales
#   * sf          <-- segundos finales
#
#   * tf          <-- tiempo final

# Algoritmo:
# aux = a
# a = b
# b = aux

import math

# Entrada de datos hora de salida
h = float(input("Introduce la hora de salida: "))
m = float(input("Introduce el minuto en el que se salida: "))
s = float(input("Introduce el segundo en el que se salida: "))
print("-------------------------------------------------")
# Entrada de datos tiempo que ha tardado en llegaer
tt = float(input("Hora a la que ha lllegado: "))
mt = float(input("minuto en el que ha lllegado: "))
st = float(input("segundo en el que ha lllegado: "))



# Cálculo
tiempo = h * 3600 + m * 60 + s # Paso la hora a la que sale a segundos
tiempot = tt * 3600 + mt * 60 + s # Paso el tiempo que tarda a segundos

tiempo = tiempot - tiempo # tiempo final en segundos

hf = tiempo / 3600
mf = (tiempo % 3600) / 60
sf = (tiempo % 3600) % 60

# Salida de datos
print("-------------------------------------------------")
print ("El cilista a tardado:", round(hf, 0) ,"horas", round(mf, 0),"minutos",round(sf, 0),"segundos")

