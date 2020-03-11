from Varias import varias
from Varias.varias import *
from Varias.varias import mostrar_array

# Generamos array aleatorio
array = genera_array_int(10, 2, 15)

# Imprimos array aleatorio por pantalla
print("La función genera un array de números  aleatorios: ")
mostrar_array(array)
#print("La función genera un array de números  aleatorios:", array2cadena(array))

print("")
print("El valor mínimo del array generado es: ", minimo_array_int(array))

print("El valor máximo del array generado es: ", maximo_array_int(array))

print("La media del array es:", media_array_int(array))

print("El número: ", esta_en_array_int(array, 10))

print("El número que buscamos esta en la poscion: ", posicion_en_array_int(array, 10))

print("El array volteado: ", voltea_array_int(array))

rota_derecha_array_int(array, 3)
print("El array rotado a la deracha: ", array)

