"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género
de la misma.
Al usuario le preguntamos si quiere un género concreto o si los quiere todos.
Usaremos la API de themoviedb.org
Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list
Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
"""
import os
import requests

URL_BASE = "https://api.themoviedb.org/3"
PETICION_TRENDING = "/trending/movie"
PETICION_GENEROS = "/genre/movie/list"
SEMANAL = "/week"
DIARIO = "/day"
pagina = 1
genero = 0
ARGS = {'api_key': '129807c4433110ade67bfb708f895d33', 'language': 'es-ES'}


def peticion(opcion, pagina, genero):
    contador_peli = 0

    url = URL_BASE + PETICION_TRENDING
    # hacer bucle while
    if opcion == 1 or opcion == 3:
        url += DIARIO
    elif opcion == 2 or opcion == 4:
        url += SEMANAL
    else:
        print("Introduce de nuevo la opción")


    while True:
        # Añado la página a ARGS
        ARGS['page'] = str(pagina)
        response = requests.get(url, params=ARGS)
        if response.status_code == 200:
            datos = response.json()
        else:
            return f"Error en la petición {response}"
        # proceso
        for p in datos['results']:
            if (genero == 0) or (genero in p['genre_ids']):
                contador_peli += 1
                print(f"{contador_peli} :  {p['title']}")
                if contador_peli == 5:
                    print("-----------------------")
                    break
        pagina += 1
        if contador_peli == 5:
            break
    print()


def mostrar_generos():
    """
    :return:
    """
    url = URL_BASE + PETICION_GENEROS

    response = requests.get(url, params=ARGS)
    if response.status_code == 200:
        print("Estado de la petición: ", response)
        datos = response.json()
    else:
        return f"Error en la petición {response}"
    print("------- Géneros -------")
    for g in datos['genres']:
        print(f"id {g['id']} - {g['name']}")
    print("-----------------------")


if __name__ == '__main__':
    # Menú principal
    while True:

        print("Esta API nos muestra el trending actual de películas.")
        print("1) Trending diario")
        print("2) Trending semanal ")
        print("3) Trending diario por género ")
        print("4) Trending semanal por género ")
        print("5) Ver géneros")
        print()
        opcion = int(input("Selecciona una opción:"))

        if opcion == 1:
            os.system("cls")
            print("Has elegido Trending diario.")
            peticion(opcion, pagina, genero)

        elif opcion == 2:
            os.system("cls")
            print("Has elegido Trending semanal.")
            peticion(opcion, pagina, genero)

        elif opcion == 3:
            os.system("cls")
            print("Has elegido Trending diario por género.")
            genero = int(input("Introduce el género: "))
            peticion(opcion, pagina, genero)

        elif opcion == 4:
            os.system("cls")
            print("Has elegido Trending semanal por género.")
            genero = int(input("Introduce el género: "))
            peticion(opcion, pagina, genero)

        elif opcion == 5:
            os.system("cls")
            mostrar_generos()


        else:
            os.system("cls")
            print("Has introducido una opción incorrecta")
            print("Vuelve a intentarlo")
