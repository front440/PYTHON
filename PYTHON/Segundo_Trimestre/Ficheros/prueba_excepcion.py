"""

    def division(numero1, numero2):
    try:
        if es_lado_correcto(numero1) and es_lado_correcto(numero2):
            return numero1 / numero2
    except ZeroDivisionError:
        print("ERROR")



def es_lado_correcto(value):
    return value <= 10
"""
def division(numero1, numero2):
    try:

            return numero1 / numero2
    except ZeroDivisionError:
        print("ERROR")


if __name__ == '__main__':
    try:
        numero1 = int(input("Introduce número 1: "))
        numero2 = int(input("Introduce numero 2: "))
    except TypeError:
        print("IWEPUTA MAMAUEBO")
    except ValueError:
        print("IWEPUTA MAMAUEBO sfd")

    division(numero1, numero2)


