# Programa: Ejercicio19_NotaFinal.py
#
# Escribir un algoritmo para calcular la nota final de un estudiante,
# considerando que por cada respuesta correcta 5 puntos, por una
# incorrecta -1 y por respuestas en blanco 0. Imprime el resultado
# obtenido por el estudiante.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 13/10/2019
#
#
# Variables a usar
#   * correcta      <-- Almacenamos preguntas correctas, valor 5
#   * incorrecta    <-- almacenamos preguntas incorrectas, valor -1
#   * notafinal    <-- Almacenamos la nota final

# Algoritmo
# notalfinal = correcta - incorrectas

# Entrada de datos
correcta = float(input("Introuzca respuestas correctas: "))
incorrecta = float(input("Introuzca respuestas incorrectas: "))


# Algoritmo
correcta = correcta * 5
incorrecta = -incorrecta * (-1)
notafinal = correcta - incorrecta

# Salida de datos
print("La nota obtenida es: ", notafinal)
