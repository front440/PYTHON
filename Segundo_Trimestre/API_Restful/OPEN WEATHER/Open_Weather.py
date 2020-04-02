import requests, json

if __name__ == '__main__':
    url = 'https://api.openweathermap.org/data/2.5/forecast'

    args = {'q': 'Cordoba,es', 'appid': '7244cf3744b6759cb242a1dda9702905', 'units': 'metric',
            'lang': 'es'}
    response = requests.get(url, params=args)
    print("Estado de la petición: ", response)
    print("Petición url: ", response.url)

    datos = response.json()
    print("Información devuelta: ", datos, "\n")

    print("----- SALIDA FORMATEADA -----")
    print("Datos tomados en:", datos['city']['name'], end=", " + datos['city']['country'])
    media = 0
    for t in datos['list']:
        fecha = t['dt_txt']


        print("El día ", t['dt_txt'], "\n hará una temperatura de: ", t['main']['temp'])
        print("La máxima es ",t['main']['temp_max'])

        media += t['main']['temp']
        print("----------")



    print("La media global es: ", media / 40)
