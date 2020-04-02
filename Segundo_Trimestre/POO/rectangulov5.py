"""
            Esta clase representa objetos de tipo rectangulo

            Atributos: base
                       altura

            Acciones: calculo del perimetro
                      calculo del area
                      saber si es igual a otro rectangulo
                      dibujar
                      comparar
"""


class DimensionRectanguloError(Exception):

    def _init_(self, mensaje_error):
        Exception._init_(self)
        self.mensaje_error = mensaje_error


class Rectangulo:
    # definimos constantes
    LADO_MAXIMO = 10
    NUM_RECTANGULOS = 0

    # creamos el constructor

    def _init_(self, base, altura):
        self.base = base
        self.altura = altura
        Rectangulo.NUM_RECTANGULOS += 1

    # esto sería el getter (observador) en java
    @property
    def base(self):
        return self.__base

    # esto sería el setter (modificador) en java
    @base.setter
    def base(self, base):
        if Rectangulo.es_lado_correcto(base):
            self.__base = base
        else:
            raise DimensionRectanguloError(f"Base incorrecta {base}")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        if Rectangulo.es_lado_correcto(altura):
            self.__altura = altura
        else:
            raise DimensionRectanguloError(f"Base incorrecta {altura}")

    # Creacion de los métodos

    def _str_(self):
        """
        Método para mostrar el rectángulo
        :return:
        """
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        return str

    def perimetro(self):
        """
        Método para calcular el perimetro
        :return:
        """
        return 2 * (self.__base + self.altura)

    def area(self):
        """
        Método para calcular el área
        :return:
        """
        return self._base * self._altura

    def es_gemelo(self, otro_rectangulo):
        """
        Método para saber si los rectángulos son iguales
        Para saber si son gemelos comparamos la base y altura de uno con el otro
        :param otro_rectangulo:
        :return: true o false
        """
        return self._altura == otro_rectangulo.altura and self._base == otro_rectangulo.base

    def compara_area(self, otro_rectangulo):
        """
        Para comparar 2 rectangulos debemos restar sus áreas
        :param otro_rectangulo:
        :return:
        """
        return self.area() - otro_rectangulo.area()

    @staticmethod
    def rectangulos_creados():
        """
        Método para saber el número de rectangulos creados
        para ello declaramos una constante y en el constructor la iniciamos y allí será donde se vayan sumando
        :return: numero de rectángulos
        """
        return Rectangulo.NUM_RECTANGULOS

    @staticmethod
    def es_lado_correcto(value):
        return type(value) == type(1) and 0 < value <= Rectangulo.LADO_MAXIMO

    def __mul__(self, other):
        """
        Multiplica la base si no se pasa del lado máximo, en ese caso lo
        hace con la altura.
        :param other: Valor entero positivo
        :return: Otro rectángulo con la superficie original*other.
        """
        assert type(other) == type(1) and other > 0  # operando correcto
        assert self.base * other <= Rectangulo.lado_maximo or self.altura * other <= Rectangulo.lado_maximo
        if self.base * other <= Rectangulo.lado_maximo:
            return Rectangulo(self.base * other, self.altura)
        else:
            return Rectangulo(self.base, self.altura * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() < other.area()

    def __le__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() <= other.area()

    def __eq__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() == other.area()


if __name__ == '__main__':

    # creamos un objeto de la clase rectangulo

    try:
        b1 = int(input("base: "))
        h1 = int(input("altura: "))
        r1 = Rectangulo(b1, h1)

        b2 = int(input("base: "))
        h2 = int(input("altura: "))
        r2 = Rectangulo(b2, h2)
    except ValueError:
        print("Solo puede poner valores enteros entre 1 y 10.")
        exit(1)
    except DimensionRectanguloError as exc:
        print("Dimensiones incorrectas.")
        print("Mensaje error:", exc.mensaje_error)
        exit(2)

    print("Test para comprobar lo métodos de la clase Rectángulo")
    print("Mostramos r1")
    print(r1)
    print("-----------------------------------------------------")
    print("Mostramos r2")
    print(r2)
    print("-----------------------------------------------------")
    print("Perímetro del rectángulo r1:", r1.perimetro())
    print("Perímetro del rectángulo r2:", r2.perimetro())
    print("-----------------------------------------------------")
    print("Área de r1: ", r1.area())
    print("Área de r2: ", r2.area())
    print("-----------------------------------------------------")
    print("¿Son los dos rectángulos iguales? ", r1.es_gemelo(r2))
    print("-----------------------------------------------------")
    print("Resultado de comparar el área de los rectángulos: ", r1.compara_area(r2))
    print("-----------------------------------------------------")
    print("¿Cuantos rectángulos tenemos? ", Rectangulo.NUM_RECTANGULOS)
