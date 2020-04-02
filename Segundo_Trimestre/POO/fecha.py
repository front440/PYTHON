"""
Colección de métodos orientados a obejtos para manejar fechas en cadenas de caracteres.
El formato de la cadena es: AAAAMMDD.
Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
Colección de funciones:
1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.
2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
   segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
   DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.
"""


class Fecha:
    def __init__(self, d, m, a):
        """
        Constructor de la clase fecha
        :param año: valor para año
        :param mes: valor para mes
        :param dia: valor para dia

        """
        assert Fecha.__es_correcta(d, m, a)
        self.__dia = d
        self.__mes = m
        self.__año = a

    # Cadena formateada
    def __str__(self):
        """
        Cadena formateada
        :return: f"{self.__dia} de {self.nombre_mes()} de {self.__año}"
        """
        return f"{self.__dia} de {self.nombre_mes()} de {self.__año}"

    def es_bisiesto(self):
        """
        Este método nos dirá si el año pasado es bisiesto
        :return:
        """
        return Fecha.__es_bisiesto(self.__año)

    def nombre_mes(self):
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        return meses[self.__mes - 1]

    # Métodos estáticos

    @staticmethod
    def __es_correcta(d, m, a):
        # ¿Son enteros?
        if not (isinstance(d, int) and isinstance(m, int) and isinstance(a, int)):
            return False
        # ¿es corecto el dia?
        elif d < 1 or d > 31:
            return False
        # ¿es correcto el mes?
        elif m < 1 or m > 12:
            return False
        # ¿es correcto el año?
        elif a < 0 or a > 9999:
            return False
        elif d == 29 and m == 2 and not Fecha.__es_bisiesto(a):
            return False
        elif
        # Si está correcto devolvemos True
        else:
            return True


    @staticmethod
    def __es_bisiesto(a):
        return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

    @staticmethod
    def __n_dias(a):
        num_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if a.__es_bisiesto :
            return num_dias[m - 1]



if __name__ == "__main__":
    while True:
        d = int(input("Día: "))
        m = int(input("Mes: "))
        a = int(input("Año: "))
        f = Fecha(d, m, a)
        print(f)
