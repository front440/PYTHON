'''
Programa: Ejercicio14_EsSubcadena.py

Autor: Francisco Javier Campos Gutiérrez

Enunciado:
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos
cadenas se introducen por teclado.



'''
estaSubcadena = False
i = 0

cadena = input("Introduce una frase: ")
subcadena = input(f"Dame una subcadena de '{cadena}': ")

comprobarHasta = len(cadena) - len(subcadena)
while not estaSubcadena and i<=comprobarHasta:
    if subcadena == cadena[i:i+len(subcadena)]:
        estaSubcadena = True
        i += 1

if estaSubcadena:
    print(f"La subcaddena {subcadena} aparece en {cadena}")
else:
    print(f"La subcadena {subcadena} no aparece en {cadena}")