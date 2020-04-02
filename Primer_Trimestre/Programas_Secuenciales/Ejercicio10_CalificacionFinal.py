# Programa: Ejercicio10_CalificacionFinal.py
#
# Proposito: Un alumno desea saber cual será su calificación final en 
# la materia de Algoritmos. Dicha calificación se compone de los 
# siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 10/10/2019
#
#
# Variables a usar
# parcial1      <-- Lee nota de parcial 1, la media de los 3 son un 55%
# parcial2      <-- Lee nota de parcial 2, la media de los 3 son un 55%
# parcial3      <-- Lee nota de parcial 3, la media de los 3 son un 55%
# parciales     <-- Almacena la media de los parciales
# examenfinal   <-- Lee nota del examen final, la nota es 30%
# trabajofinal  <-- Lee nota del trabajo final, la nota es 15%
# notafinal     <-- La nota final haciendo los calculos de todos los examenes y parciales


# Algoritmo:
# parciales     <-- ((parcial1 + parcial2 + parcial3)/3) * 0.55
# examenfinal   <-- examenfinal * 0.3
# trabajofinal  <-- trabajofinal * 0.15
# notafinal     <-- parciales + examenfinal + trabajofinal

# Datos parciales
parcial1 = float(input("Introduce la nota del parcial 1: "))
parcial2 = float(input("Introduce la nota del parcial 2: "))
parcial3 = float(input("Introduce la nota del parcial 3: "))
print("--------------------------------------------")

# Cáculo de parciales
parciales = ((parcial1 + parcial2 + parcial3)/3) * 0.55 # hacemos la media de los parciales

# Salida parciales
print("La nota de los parciales sobre la evaluacion es ",parciales," sobre la evaluación") # Lo indicamos por pantalla
print("--------------------------------------------")

# Datos de examen final
examenfinal = float(input("Ingresa la nota del examen final: "))
examenfinal = examenfinal * 0.3  # Calculamos el porcentaje que tendra el examen final sobre al evaluación.

# Salida de examen final
print("--------------------------------------------")
print("La nota del examen final tendra una puntación de: ", examenfinal,"sobre la evaluación.")
print("--------------------------------------------")


# Datos trabajo final
print("--------------------------------------------")
trabajofinal = float(input("Introduce la nota del trabajo final:"))
print("--------------------------------------------")

trabajofinal = trabajofinal * 0.15 # Culculamos el porcentaje que tendra el trabajo final sobre la evaluación

# Salida de trabajo final
print("--------------------------------------------")
print("La nota del trabajo final tendra una puntuación de ", trabajofinal,"sobre la evaluación.")
print("--------------------------------------------")

# Cáculo final de parciales, examen final y trabajo final
notafinal = parciales + examenfinal + trabajofinal

# Salida nota final
print("--------------------------------------------")
print("La nota del alumno es:", notafinal)
print("--------------------------------------------")
print("--------------------------------------------")
