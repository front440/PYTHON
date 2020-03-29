"""
2. Crea una clase Fraccion (Python) de forma que podamos hacer las siguientes operaciones:

    Contruir un objeto Fraccion pasándole el numerador y el denominador.
    Obtener la fracción como cadena de caracteres.
    Obtener y modificar numerador y denominador. No se puede dividir por cero.
    Obtener resultado de la fracción (número real).
    Multiplicar la fracción por un número.
    Multiplicar, sumar y restar fracciones.
Simplificar la fracción.
"""

class Fraccion:
    '''
    Método constructor de la clase.
    '''
    
    def __init__(self, numerador, denominador):
        '''
        
        :param numerador: 
        :param denominador: 
        '''
        self.__numerador = numerador
        self.__denominador = denominador

    #Propiedades. Getter y setter.
    @property
    def numerador(self):
        return self.__numerador
    
    @numerador.setter
    def numerador(self, value):
        self.__numerador = value
        
    @property
    def denominador(self):
        return self.__denominador
    
    @denominador.setter
    def denominador(self, value):
        try:
           if self.__denominador > 0:
                self.__denominador = value

        except ZeroDivisionError:
            print("No se puede dividir entre 0")
            exit(1)
    '''
        if self.__denominador != 0:
            self.__denominador = value
        else:
            print("No se puede dividir por 0.")
    '''

    #Metodos
    def __str__(self):
        return f"{self.__numerador} / {self.__denominador}"

    def resultado(self):
        '''

        :return: numerador entre denominador
        :exception division entre 0 no se puede calcular.
        '''

        try:
            return self.__numerador / self.__denominador
        except ZeroDivisionError:
            print("El denominador no puede ser 0.")

    def multiplica_por_entero(self, numero):
        return f"{self.numerador * numero} / {self.denominador}"

    def multiplica_por_otra_fraccion(self, otra_fraccion):
        return  f"{self.numerador * otra_fraccion.numerador} / {self.denominador * otra_fraccion.denominador}"

    def suma_fraccion(self,otra_fraccion):
        return f"{self.numerador * otra_fraccion.denominador + self.denominador * otra_fraccion.numerador} / {self.denominador * otra_fraccion.denominador}"

    def resta_fraccion(self,otra_fraccion):
        return f"{self.numerador * otra_fraccion.denominador - self.denominador * otra_fraccion.numerador} / {self.denominador * otra_fraccion.denominador}"

    def simplifica_fraccion(self):
        mcd = self.mcd()
        self.numerador //= mcd
        self.denominador //= mcd

    # @staticmethod
    def mcd(self):
        resto_division = self.numerador % self.denominador
        while resto_division != 0:
            self.denominador = resto_division
            resto_division = self.numerador % self.denominador
        maximo = self.denominador
        return maximo


if __name__ == '__main__':
    f1 = Fraccion(60,48)
    f2 = Fraccion(9,10)

    print("Mostramos fraccion 1 y 2.")
    print("Fraccion f1: ",f1)
    print("Fraccion f2: ",f2)
    print()
    print("Mostramos el resultado de la fraccion f1:", f1.resultado())
    print("Mostramos el resultado de la fraccion f2:", f2.resultado())
    print()
    numero = int(input("Introduce un núemro para multiplicar a la fraccion f1: "))
    print(f"Resultado de multiplicar {f1} por {numero}: ", f1.multiplica_por_entero(numero))
    print(f"Resultado de multiplicar {f2} por {numero}: ", f2.multiplica_por_entero(numero))
    print()
    print(f"Resultado de multiplicar la fraccion {f1} por otra fraccion: ", f1.multiplica_por_otra_fraccion(f2))
    print(f"Resultado de multiplicar la fraccion {f2} por otra fraccion: ", f2.multiplica_por_otra_fraccion(f1))
    print()
    print(f"Resultado de sumar {f1} + {f2}: ", f1.suma_fraccion(f2))
    print(f"Resultado de sumar {f2} + {f1}: ", f2.suma_fraccion(f1))
    print()
    print(f"Resultado de restar {f1} - {f2}: ", f1.resta_fraccion(f2))
    print(f"Resultado de restar {f2} - {f1}: ", f2.resta_fraccion(f1))
    f1.simplifica_fraccion()
    print(f"Resultado de simplificar la fraccion {f1}: ",f1)
    f2.simplifica_fraccion()
    print(f"Resultado de simplificar la fraccion {f2}: ",f2)



    
    