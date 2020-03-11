class Fraccion:

    """
    Crea una clase Fracción (Python) de forma que podamos hacer las siguientes operaciones:

    - Contruir un objeto Fraccion pasándole el numerador y el denominador.
    - Obtener la fracción como cadena de caracteres.
    - Obtener y modificar numerador y denominador. No se puede dividir por cero.
    - Obtener resultado de la fracción (número real).
    - Multiplicar la fracción por un número.
    - Multiplicar, sumar y restar fracciones.
    - Simplificar la fracción.
    """

    # Constructor
    def __init__(self, numerador, denominador):
        """
        Constructor de la clase fraccion
        :param numerador: Representa al numerador
        :param denominador: Representa al denominador
        """
        self.__numerador = numerador
        self.__denominador = denominador


    # Getters de numerador
    @property
    def numerador(self):
        return self.__numerador

    # Setters de numerador
    @numerador.setter
    def numerador(self, value):
        self.__numerador = value

    # Getters de denominador
    @property
    def denominador(self):
        return self.__denominador

    # Setters de denominador
    @denominador.setter
    def denominador(self, value):
        if value != 0:
            self.__denominador = value
        else:
            print("Denominador nunca puede ser 0.")

    # Métodos

    # Salida formateada
    def __str__(self):
        """
        Salida formateada de la fracción
        :return:
        """
        return f"{self.__numerador} / {self.__denominador}"

    # Resultador real de la fracción
    def resultado_real(self):
        """
        Muestra El resulado de la fracción, es decir, numerador entre denominadoar
        :return: número real
        """
        return self.__numerador / self.__denominador

    # Multiplicar fracción por un número
    def multiplicar_por_numero(self, numero):
        """
        Multiplicamos la fracción creada por número pasado por parámetro
        :param numero:
        :return:
        """
        return (self.__numerador / self.__denominador) * numero

    # Multiplicar fracción
    def multiplicar_fraccion(self, otra):
        """
        Multiplicamos una fracción y otra por parámetro
        :param otra: fracción
        :return:
        """
        self.__numerador *= otra.numerador
        self.__denominador *= otra.denominador

    # Hallamos mínimo común múltiplo
    """
    def mcm(self, otra):
        
        Resolvemos mínimo común múltiplipo
        :param otra:
        :return:
        
        maximo = max(self.__denominador, otra.denominador)

        while True:
            if maximo % otra.denominador == 0 and maximo % self.__denominador == 0:
                return maximo
            maximo += 1
    """

    # Suma de fracciones
    def suma_fraccion(self, otra):
        """
        Empleamos el algoritmo para hallar la suma de la fracción.
        :param otra:
        :return:
        """
        self.__numerador = (self.__numerador * otra.denominador) + (self.__denominador * otra.numerador)
        self.__denominador = (self.__denominador * otra.denominador)

    # Resta de fracciones
    def resta_fraccion(self, otra):
        """
        Resta de fracción, pasada como parámetro
        :param otra:
        :return:
        """
        self.__numerador = (self.__numerador * otra.denominador) - (self.__denominador * otra.denominador)
        self.__denominador = (self.__denominador * otra.denominador)

    # Máximo común divisor
    def __mcd(self):
        """
        Este método nos devolvera el máximo común divisor del numerador y denomirador
        :return: mcd
        """
        dividendo = self.__numerador
        divisor = self.__denominador
        resto = dividendo%divisor

        while resto !=0:
            dividendo = divisor
            divisor = resto
            resto = dividendo%divisor
            mcd = divisor
        return mcd

    # Método para simplificar fracción
    def simplifica(self):
        """
        Simplifica la fracción partiendo del mcd.
        """
        mcd = self.__mcd()
        self.__numerador //= mcd
        self.__denominador //= mcd

if __name__ == "__main__":

    print("Pruebas de fracción")
    f1 = Fraccion(5, 2)
    print("Creamos fraccion ", f1)

    print("Mostramos resultado")
    print(f1.resultado_real())

    print("Multiplicamos fracción ",f1 ," por 2")
    print(f1.multiplicar_por_numero(2))

    print("Creamos f2")
    f2 = Fraccion(5, 2)

    print(f2)
    print("Multiplicamos fracción ", f1, " por ", f2)
    f1.multiplicar_fraccion(f2)
    print("Resultado: ", f1.resultado_real())

    f3 = Fraccion(7, 3)
    f4 = Fraccion(8, 4)
    print("Sumar fracciónes")
    print(f"El resultado de  {f3.denominador} y {f4.denominador} es:")
    f3.suma_fraccion(f4)
    print("La suma de la fracciones es: ")
    print(f3)

    # Restamos fracciones
    f5 = Fraccion(4,6)
    f6 = Fraccion(7,2)
    print(f"Creamos la fraccion {f5} y {f6}")
    f5.resta_fraccion(f6)
    print("El resultado de la fracción es:")
    print(f5)

    print("Simplificamos fraccion", f5)
    f5.simplifica()
    print("Resultado", f5)



