class Tiempo:
    """
    Esta clase representa objetos de tipo tiempo
    Acciones:
    - Sumar y restar otros objetos de tiempo
    - Sumar, restar horas, minutos y segundos
    - Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
    """

    def __init__(self, hora, minuto, segundo):
        """
        Constructor de la clase tiempo
        Lanza una excepción en caso de valores incorrectos
        :param hora: Representa una hora
        :param minuto: Representa un minuto
        :param segundo: Representa un segundo
        """
        # Excepción para evitar que el tiempo sea inconsistente
        assert hora >= 0 and 0 <= minuto <= 60 and 0 <= segundo <= 60
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    # Setter o modificadores
    @property
    def hora(self):
        return self.__hora

    @property
    def minuto(self):
        return self.__minuto

    @property
    def segundo(self):
        return self.__segundo

    # Mostramos cadena formateada
    def __str__(self):
        """
        Muestra cadena formateada
        :return: 1h 1m 1s
        """
        return f"{self.__hora}h {self.__minuto}m {self.__segundo} s"

    # Sumar tiempo
    def sumar_tiempo(self, otro):
        """
        Sumará otro tiempo insertado como parámetro
        :return:
        """
        tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo + otro.hora * 3600 + otro.minuto * 60 + otro.segundo
        self.__convertidor(tiempo_total)

    # Restar tiempo
    def restar_tiempo(self, otro):
        """
        Sumará otro tiempo insertado como parámetro
        :return:
        """
        tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo - (
                    otro.hora * 3600 + otro.minuto * 60 + otro.segundo)
        self.__convertidor(tiempo_total)

    # Sumar horas pasado como parámetro
    def sumar_horas(self, horas):
        """
        Método para sumar horas, si el resultado es negativo lanza excepción
        :param horas:
        :return:
        """
        assert self.__hora + horas >= 0
        self.__hora += horas

    # Restar horas pasado como parámetro
    def resta_horas(self, horas):
        """
        Método para restar horas, si el resultado es negativo lanza excepción
        :param horas:
        :return:
        """
        assert self.__hora - horas >= 0
        self.__hora -= horas

    # Sumamos minutos como parámetro
    def sumar_minutos(self, minutos):
        """
        Sumamos minutos pasado como parámetro, si las horas finales son negativas lanza
        una excepción
        :param minutos:
        :return:
        """
        if minutos >= 0:
            tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo + minutos * 60
            self.__convertidor(tiempo_total)
        else:
            print("Parámetro erroneo")

    # Restamos minutos como parámetro
    def restar_minutos(self, minutos):
        """
        Restar minutos pasados como parámetro
        :param minutos:
        :return:
        """
        if minutos >= 0:
            tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo - minutos * 60
            self.__convertidor(tiempo_total)
        else:
            print("Parámetro erroneo")

    # Sumar segundos pasados como parámetro
    def sumar_segundos(self, segundos):
        """
        Sumar segundos pasados como parámetro
        :param segundos:
        :return:
        """
        if segundos >= 0:
            tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo + segundos
            self.__convertidor(tiempo_total)
        else:
            print("Parámetro erroneo")

    # Restar segundos pasados como parámetro
    def restar_segundos(self, segundos):
        """
        Restamos segundos pasado como parámetro
        :param segundos:
        :return:
        """
        if segundos >= 0:
            tiempo_total = self.__hora * 3600 + self.__minuto * 60 + self.__segundo - segundos
            self.__convertidor(tiempo_total)
        else:
            print("Parámetro erroneo")

    # Método conversor de segundos a horas, minutos y segundos
    @staticmethod
    def __convertidor(self, tiempo_total):
        """
        Este método nos ayudará a pasar el tiempo total  (segundos) a las horas, minutos y segundos
        :param tiempo_total: tiempo total en segundos
        :return:
        """
        self.__hora = tiempo_total // 3600
        self.__minuto = (tiempo_total % 3600) // 60
        self.__segundo = (tiempo_total % 3600) % 60


if __name__ == "__main__":
    # Pruebas de la clase tiempo

    # Creamos instancia de tiempo
    tiempo1 = Tiempo(20, 23, 12)
    tiempo2 = Tiempo(2, 2, 2)

    # Mostramos instancias
    print("Mostramos tiempo1 y tiempo2")
    print(tiempo1)
    print(tiempo2)

    # Sumamos instancias
    print("Sumamos instancias")
    print("tiempo1", tiempo1, " y tiempo2 ", tiempo2)
    tiempo1.sumar_tiempo(tiempo2)
    print(tiempo1)

    # Restamos instancias
    print("Restamos instancias")
    print("tiempo1", tiempo1, " y ", "tiempo2", tiempo2)
    tiempo1.restar_tiempo(tiempo2)
    print("Resultado", tiempo1)

    # Método sumar horas
    print("Método sumar horas")
    print("tiempo1", tiempo1)
    tiempo1.sumar_horas(20)
    print("Resultado", tiempo1)

    # Método restar horas
    print("tiempo1", tiempo1)
    tiempo1.resta_horas(5)
    print(tiempo1)

    # Método sumar  minutos
    print("Sumar minutos tiempo1 ", tiempo1)
    tiempo1.sumar_minutos(7)
    print("Resultado", tiempo1)

    # Método restar minutos
    print("Restar minutos tiempo1 ", tiempo1)
    tiempo1.restar_minutos(7)
    print("Resultado", tiempo1)

    # Método sumar segundos
    print("Sumar segundos tiempo1", tiempo1)
    tiempo1.sumar_segundos(22)
    print("Resultado", tiempo1)

    # Método restar segundos
    print("Sumar segundos tiempo1", tiempo1)
    tiempo1.restar_segundos(22)
    print("Resultado", tiempo1)
