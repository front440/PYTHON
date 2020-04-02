"""
1. Modifica el ejercicio 1 del tema anterior de manera que:

- El programa admita dos parámetros:
    - El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la
ciudad es errónea el programa termina con un mensaje de error y código 2.
    - El segundo es opcional, y si existe es el directorio donde vamos a crear un fichero
html con la información formateada como una tabla del pronóstico de la temperatura, si
no existe la información se muestra por pantalla. Consideraciones:
        - este fichero tendrá por nombre: {CIUDAD}{FECHA-INICIO}{FECHA_FIN},
ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html"
        - si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
    - Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de
error (código 1) diciendo que la sintaxis es incorrecta.
    - Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto
explicando qué hace.
"""
import requests, sys, os

ciudad = ""
URL_BASE = "https://api.openweathermap.org/data/2.5/forecast?"
ARGS = {'q': ciudad, 'appid': '7244cf3744b6759cb242a1dda9702905', 'lang': 'es', 'units': 'metric'}
ruta = "D:/DAW/DAW19-20/PROGRAMACION/PYTHON/"


def peticion(ciudad):
    """
    Método que hará petición get a la API
    :param ciudad:
    :return:
    """

    URL_BASE = "https://api.openweathermap.org/data/2.5/forecast?"
    ARGS = {'q': ciudad, 'appid': '7244cf3744b6759cb242a1dda9702905', 'lang': 'es', 'units': 'metric'}

    response = requests.get(url=URL_BASE, params=ARGS)
    # Comprobamos que el estado sea 200, sino salimos del programa.
    if response.status_code != 200:
        print(f"Error en la petición, error {response.status_code}", file=sys.stderr)

    # En caso contrario devolvemos contenido de la petición
    else:
        datos = response.json()
        return datos


def mostrar_html(ciudad, directorio):
    # Nombre del fichero donde guardaremos la mediciones
    # este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN},
    # ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
    nombre_archivo = ciudad + "_" + peticion(ciudad)['list'][0]['dt_txt'] + "_" + peticion(ciudad)['list'][-1][
        'dt_txt'] + ".html"

    # Reemplazamos los ':' por '.' y los espacios por '-'
    nombre_archivo.replace(":", ".").replace(" ", "-")

    # Formamos la ruta completa                 COMPROBAR S.O.
    ruta_completa = directorio + "\\" + nombre_archivo

    # Comprobamos antes de si el fichero existe, si el fichero existe, no lo creamos.
    if open(ruta_completa, "r"):
        # ¿Quieres machacar el archivo? Hacer con while true
        print("El fichero existe, la información será mostrada por pantalla")
        obtener_datos(ciudad)
    else:
        manejador = open(ruta_completa, "w")

        # Realizas petición

        manejador.write(f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lectura de temperaturas en {ciudad}</title>
</head>
<body>
    <center><p>Este programa nos muestra los resultados de las mediciones para los próximos 5 días en {ciudad}</p>
        <table border="1">
            <tr>
                <th>Día</th>
                <th>Temperatura Media</th>
                <th>Temperatura Mínima</th>
                <th>Temperatura Máxima</th>
                <th>Nº Mediciones</th>
            </tr>
            <tr>
                <td><center>{dia}</center></td>
                <td><center>{temp_med:.2f}º</center></td>
                <td><center>{temp_min}º</center></td>
                <td><center>{temp_max}º</center></td>
                <td><center>{mediciones}</center></td>
            </tr>
            <tr>
                <th><center>TOTALES</center></th>
                <th><center>{temp_med:.2f}º</center></th>
                <th><center>{temp_min}º</center></th>
                <th><center>{temp_max}º</center></th>
                <th><center>{mediciones}</center></th>
            </tr>
        </table>
    </center>
</body>
</html>
        """)
        manejador.close()


def ayuda():
    """
    :return: Devuelve información del programa.
    """
    print("""
El programa nos mostrará el pronóstico de la temperatura de la ciudad introducida.
- El primer parámetro será la ciudad de la cual queramos saber el pronóstico, indicando
    las dos primeras letras del país separado con una coma si la ciudad corresponde con otro país.
- El segundo parámetro será opcional y este será la ruta donde guardará el archivo
    html con los datos guardados. En caso de no añadir segundo parámetro los datos serán
    directamente mostrados por pantalla.
    """)
    exit(0)


def obtener_datos(ciudad, directorio):
    """
    Método que mostrará los datos de la petición por pantalla
    :param ciudad:
    :return:
    """
    # Llamamos a la petición
    datos = peticion(ciudad)

    # cálculos
    dias = dict()  # diccionario con clave el día y valor la lista de mediciones del día
    totales = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días

    # Recorremos el fichero json en busca de los datos
    for medicion in datos["list"]:
        # fecha y temperatura de la medición
        dia = medicion["dt_txt"][:10]
        temp = float(medicion["main"]["temp"])
        temp_min = float(medicion["main"]["temp_min"])
        temp_max = float(medicion["main"]["temp_max"])

        # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
        if not dias.get(dia):
            dias[dia] = {"temp": [], "temp_min": [], "temp_max": []}
        # añadimos medición
        dias[dia]["temp"].append(temp)
        dias[dia]["temp_min"].append(temp_min)
        dias[dia]["temp_max"].append(temp_max)
        totales["temp"].append(temp)
        totales["temp_min"].append(temp_min)
        totales["temp_max"].append(temp_max)

    if directorio == "":
        # resultados
        for dia, temps in dias.items():
            # diario
            temp_med = sum(temps['temp']) / len(temps['temp'])
            temp_min = min(temps['temp_min'])
            temp_max = max(temps['temp_max'])

            print(
                f"Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}:  Temperatura media: {temp_med:.2f}º, mínima: {temp_min}º y máxima: {temp_max}º. Mediciones: {len(temps['temp'])}")

        # global
        temp_med = sum(totales['temp']) / len(totales['temp'])
        temp_min = min(totales['temp_min'])
        temp_max = max(totales['temp_max'])

        print(f"TOTALES:        Temperatura media: {temp_med:.2f}º, mínima: {temp_min}º y máxima: {temp_max}º")
    else:
        mostrar_html()


if __name__ == '__main__':

    # Comprobamos parámetros
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Número de parámetros introducido incorrecto", file=sys.stderr)
        exit(1)

    # Si el número de parámetros es dos, quiere decir que solo hemos introducido la ciudad
    if len(sys.argv) == 2:
        ciudad = sys.argv[1]
        # Si la ciudad es introducida es '-h' mostraremos la información del programa
        if ciudad == "-h":
            ayuda()
        print(obtener_datos(ciudad, ""))
    # Si el número de parámetros es 3, quiere decir que hemos introducido la ciudad y el directorio.

    elif len(sys.argv) == 3:
        ciudad = sys.argv[1]
        directorio = sys.argv[2]
        mostrar_html(ciudad, directorio)
