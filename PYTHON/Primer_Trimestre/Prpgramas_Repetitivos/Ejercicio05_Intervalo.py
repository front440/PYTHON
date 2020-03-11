# Programa: Ejercicio05_Intervalo.py
#
# Proposito: Escribe un programa que pida el limite inferior y superior
# de un intervalo. Si el límite inferior es mayor que el superior lo
# tiene que volver a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos
# el 0. Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 28/10/2019
#
# Variables, algoritmos a usar
#   * fuera_intervalo  <-- Almacenaremos los números fuera del intervalo
#   * total_suma       <-- Sumaremos todos los numeros dentro del intervalo
#   * igual_intervalo  <-- Almacenamos el numero de veces que se ha repetido el número igual al intervalo
#   * num              <-- Almacenamos números introducidos
#   * total_suma       <-- Almacenaremos la suma de todos los numeros

# Analisis, Algoritmos
# Este programa nos pedirá un numero mayor que otro para crear un
# intervalo. El número menor nunca podrá ser mayor que el número mayor.
# Iremos introduciendo una serie de números, los que queramos y debemos
# indicar la suma de ellos. Tambien Si hemos introducido alguno igual
# al intervalo y si hemos introducido números fuera de él. El programa
# acabará con un 0.

# Leer datos

fuera_intervalo = 0
total_suma = 0
igual_intervalo = 0

print("Este programa nos permitirá calcular la suma de los números introducidos entre un intervalo.")
print("además, de los numeros escritos fuera él.")
print("-----------------------------------------------------------------")

num_superior = float(input("Introduce el número para el intervalo mayor: "))
num_inferior = float(input("Introduce el número para el intervalo menor: "))

# Creamos un bucle para que el número menor no sea el mayor.
while num_inferior > num_superior:
    print("El intervalo menor no puede ser que el intervalo mayor:")
    num_inferior = float(input("Introduce el número para el intervalo menor: "))
    
print("-----------------------------------------------------------------")
# Volvemos a crear un bucle, esta vez creamos la sentencia distinto a 0
# para poder seguir con los algoritmos.
print("Introduciendo el número 0, terminaremos con el programa")
num = float(input("Introduce números para realizar la suma: "))
while num != 0:
    if num > num_inferior and num < num_superior: # si el número introducido esta entre el intervalo los sumamos.
        total_suma = total_suma + num
    else:
        fuera_intervalo += 1 # si el numero esta fuera del intervalo, decimos que esta fuera del intervalo.
    num = float(input("Introduce números para realizar la suma: "))
    if num_inferior == num or num_superior == num:
        igual_intervalo += 1
        
# Mostramos resultados
print("-----------------------------------------------------------------")
    
print(f"La suma de los números introducidos es {total_suma}")
print(f"Hay un total de {fuera_intervalo} fuera del intervalo")
print(f"Hay {igual_intervalo} igual al numero mayor o menor del intervalo ")
    
    
    
    
    
    
    
    
    

