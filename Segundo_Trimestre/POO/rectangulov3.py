class Rectangulo:
    """
    Versión 3.0.
    Esta clase representa objetos de tipo rectángulo.
    Acciones: cálculo del perímetro, área, dibujar, comparar.
    Mejoras respecto a la versión 2:
    - Quitamos getters y setters estilo Java y los sustituimos por propiedades.
    - Usaremos métodos privados y estáticos.
    - Usaremos variables de instancia de clase.
    """
    lado_maximo = 10        # lado máximo del rectángulo
    __num_rectangulos = 0   # contador de rectángulos creados

    def __init__(self, base, altura):
        """
        Constructor de la clase.
        :param base: base del rectángulo.
        :param altura: altura del rectángulo.
        """
        self.__base = 1
        self.__altura = 1
        Rectangulo.__num_rectangulos += 1
        # por si hubiera errores en los parámetros hemos dado valor inicial
        self.base = base
        self.altura = altura

    # propiedades

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        if self.es_lado_correcto(value):
            self.__base = value
        else:
            # Mucho mejor sería lanzar una excepción
            print("ERROR. Base incorrecta")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        if Rectangulo.es_lado_correcto(value):
            self.__altura = value
        else:
            # Mucho mejor sería lanzar una excepción
            print("ERROR. Altura incorrecta")

    # resto métodos

    @staticmethod
    def num_rectangulos():
        return Rectangulo.__num_rectangulos

    @staticmethod
    def es_lado_correcto(value):
        return type(value)==type(1) and 0<value<=Rectangulo.lado_maximo

    def perimetro(self):
        """
        :return: perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def area(self):
        """
        :return: área del rectángulo.
        """
        return self.base * self.altura

    def compara(self, otro):
        """
        Compara nuestro rectángulo con otro.
        :param otro: objeto con el que comparamos el actual.
        :return: >0 si mayor, 0 si igual, <0 si menor.
        """
        return self.area() - otro.area()

    def es_gemelo(self, otro):
        """
        Comprueba si el objeto pasado es el mismo rectángulo, o sea,
        tiene la misma base y altura.
        :param otro: objeto con el que comparamos el actual.
        :return: True o False
        """
        return self.base == otro.base and self.altura == otro.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo.
        """
        print(self)

    # métodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        str = str[:-1]
        return str



if __name__ == "__main__":
    r1 = Rectangulo(4, 1)
    r2 = Rectangulo(3, 2)
    print(f"Probamos clase rectángulo con r1: ({r1.base},{r1.altura}) y "
          f"r2: ({r2.base},{r2.altura})\n")
    # mostramos
    r1.muestra()
    print()
    r2.muestra()
    # comparamos
    print("Resultado de comparar r1 con r2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))
    # magnitudes
    print("Área r1:", r1.area(), "Perímetro r1:", r1.perimetro())
    print("Área r2:", r2.area(), "Perímetro r2:", r2.perimetro())
    # accedemos a variables de instancia de clase
    print("Rectángulos creados", Rectangulo.num_rectangulos())