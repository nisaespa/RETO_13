import requests  # Librería para realizar solicitudes HTTP
import json      # Librería para trabajar con formato JSON
# función para obtener datos JSON de una API dada la URL
def obtener_json(api_url):
    # Realizar una solicitud GET a la API
    response = requests.get(api_url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Devolver los datos JSON si la solicitud fue exitosa
        return response.json()
    else:
        # Imprimir un mensaje de error si la solicitud falló
        print(f"Error al obtener datos de {api_url}")
        return None
# Ejemplos de URLs de API
api_url_1 = "https://api.publicapis.org/entries"
api_url_2 = "https://catfact.ninja/fact"
api_url_3 = "https://api.coindesk.com/v1/bpi/currentprice.json"
# Obtener datos JSON de las API utilizando la función definida anteriormente
json_data_1 = obtener_json(api_url_1)
json_data_2 = obtener_json(api_url_2)
json_data_3 = obtener_json(api_url_3)
# Imprimir los datos JSON obtenidos con formato indentado
print("Datos de la API 1:")
print(json.dumps(json_data_1, indent=2))
print("\nDatos de la API 2:")
print(json.dumps(json_data_2, indent=2))
print("\nDatos de la API 3:")
print(json.dumps(json_data_3, indent=2))
# función para extraer y mostrar los pares clave: valor de un diccionario JSON
def extraer_pares(json_data):
    if json_data:
        # Iterar sobre los pares clave: valor y mostrarlos
        for key, value in json_data.items():
            print(f"{key}: {value}")
# Extraer y mostrar los pares clave: valor de los datos obtenidos de cada API
print("\nPares de llave : valor de la API 1:")
extraer_pares(json_data_1)
print("\nPares de llave : valor de la API 2:")
extraer_pares(json_data_2)
print("\nPares de llave : valor de la API 3:")
extraer_pares(json_data_3)
