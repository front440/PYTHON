# Programa: Fibonacci.py
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Analisis: Este programa nos permitirá saber a que número de la secuencia
# de Fibonacci correspone, con el número que insertamos.
#
# Variables:
# posicion	<-- Número insertado para saber el número que correspone a la
#				secuencia de fibonacci
# nactual	<-- Es el resultado de el número anterior y el auxiliar
# nanterior	<-- Número anterior al actual
# aux		<--

nactual = 0
nanterior = 1
aux = 0

print("Es programa nos permite saber la secuencia de fibonacci")

n = int(input("Introduce el número de la secuencia que quieras saber: "))

for i in range (0,n):
    print(f"Probando número fibonnaci: {nactual}")
    aux = nactual
    nactual = nactual + nanterior
    nanterior = aux
