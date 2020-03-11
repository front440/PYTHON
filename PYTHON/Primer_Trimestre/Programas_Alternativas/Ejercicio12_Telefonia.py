# Programa: Ejercicio12_Telefonoa.py
#
# Proposito: ULa política de cobro de una compañía telefónica es: 
# cuando se realiza una llamada, el cobro es por el tiempo que ésta 
#dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los 
# siguientes tres, 80 céntimos, los siguientes dos minutos, 70
# céntimos, y a partir del décimo minuto, 50 céntimos. 
# Además, se carga un impuesto de 3 % cuando es domingo, y si es
# otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %.
# Realice un algoritmo para determinar cuánto debe pagar por cada
# concepto una persona que realiza una llamada.
#
# Autor: Francisco Javier Campos Gutiérrez
#
# Fecha : 18/10/2019
#
# Variables, algoritmos a usar
#   * m     <-- Variable para almacenar los minutos de la llamada
#   * p     <-- Variable para almaccenar el precio final de la llamada

# Analisis, Algoritmos
# La compañia irá cobrando la llamada según siga en curso, es decir, que
# con medida que vaya subiendo de minutos se irán aplicando las tarifas.
# Dice:
# Los primeros 5 minutos a 1€ :      m > 5  <-- m * 1€
# Del minuto 5 al 8 a 80cnt:         m > 8  <-- m + m * 0.8
# Del minuto 8 al 10 a 70cnt:        m > 10 <-- m + m * 0.7
# Del minuto 10 en adelante 50cnt:   10 < m <-- m + m * 0.5
# También nos cuenta que se le aplicará un recargo:
# de lunes a sabado:
# mañana    <-- 15%
# tarde     <-- 10%
# Domingo   <-- 3%

# Leer datos


print("Este programa determinará el precio de una llamada telefónica.")
print("-----------------------------------------------------------------")

m = float(input("¿Cuantos minutos ha durado la llamada?"))

print("-----------------------------------------------------------------")
print("¿Qué día de la semana ha hecho la llamada?")

# Menu para elegir día de la semana
print("1) Lunes")
print("2) Martes")
print("3) Miercoles")
print("4) Jueves")
print("5) Viernes")
print("6) Sabado")
print("7) Domingo")

d = float(input("Indique el día"))
print("-----------------------------------------------------------------")

print("La llamada ¿ha hecho de mañana o de tarde?")

# Menu para elegir día de la semana
print("1) Mañana")
print("2) Tarde")


t = float(input("Introduce cuando te ha producido la llamada"))
print("-----------------------------------------------------------------")

# Desarrollo, precio por minuto

if m < 5:
    print("La llamada tiene un precio base de: ",  m * 1)
    if m > 5 and m < 8:
        print("La llamada tiene un precio base de: ",  m*0.8+5-5)
    elif m > 8 and m < 10:
        print("La llamada tiene un precio base de: ", m*0.7+5+2.4-8)
    else:
        print("La llamada tiene un precio base de: ", m*0.5+5+2.4+1.4-10)
if d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 and t == 1:
    print("El coste de la llamada es",m + m*0.15)
elif d == 1 or d == 2 or d == 3 or d == 4 or d == 5 or d == 6 and t == 2:
    print("El coste de la llamada es: ", m + m*0.10)
else:
    print("El coste de la llamada es: ", m + m*0.03)
