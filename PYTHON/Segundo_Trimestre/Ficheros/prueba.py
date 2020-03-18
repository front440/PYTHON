import pickle

import requests

if __name__ == '__main__':
    # ciudad = input("Ciudad de la que quiere conocer el pronóstico del tiempo en los próximos 5 días: ")

    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": "london", 'appid': '7244cf3744b6759cb242a1dda9702905', "units": "metric", "lang": "es"}

    response = requests.get(url, params=params)
    datos = response.json()

    # petición

    for m in datos['list']:

        nombre_archivo = (m[0]["dt_txt"][:10])
        temperatura_max = m['main']['temp']

    f = open(dia+".html", 'w')
    mensaje = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

        <html xmlns="http://www.w3.org/1999/xhtml">

            <head>

                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                 
                <title>Demystifying Email Design</title>
                 
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

            </head>
            
            <body>
            
            <h1> temperatura maxima {dia}
            
            <table>
                  <tr>
                    <th></th>
                    <th></th>
                    <th></th>
                    <th></th>
                    <th></th>
                    <th></th>
                  </tr>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                </table>
            
            </body>

            </html>
"""
    f.write(mensaje)
    f.close()
