# Importamos el módulo json para trabajar con datos en formato JSON
import json
# función para cargar datos desde un archivo JSON
def cargar_json(nombre_archivo):
    # Abrimos el archivo en modo de lectura ('r')
    with open(nombre_archivo, 'r') as archivo:
        # Cargamos los datos desde el archivo JSON
        datos = json.load(archivo)
    # Devolvemos los datos cargados
    return datos
# función para obtener nombres de personas que practican un deporte específico
def obtener_nombres_por_deporte(json_data, deporte):
    # Inicializamos una lista para almacenar nombres
    nombres = []
    # Iteramos sobre los datos JSON
    for usuario, info in json_data.items():
        # Verificamos si el deporte está en la lista de deportes del usuario
        if deporte in info["deportes"]:
            # Agregamos el nombre completo a la lista
            nombres.append(info["nombres"] + " " + info["apellidos"])
    # Devolvemos la lista de nombres
    return nombres
# función para obtener nombres de personas en un rango de edad específico
def obtener_nombres_por_rango_edad(json_data, edad_min, edad_max):
    # Inicializamos una lista para almacenar nombres
    nombres = []
    # Iteramos sobre los datos JSON
    for usuario, info in json_data.items():
        # Verificamos si la edad del usuario está dentro del rango especificado
        if edad_min <= info["edad"] <= edad_max:
            # Agregamos el nombre completo a la lista
            nombres.append(info["nombres"] + " " + info["apellidos"])
    # Devolvemos la lista de nombres
    return nombres
# Verificamos si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Especificamos el nombre del archivo JSON
    nombre_archivo = "jaison.json"  # Reemplaza con el nombre de tu archivo JSON
    # Cargamos los datos desde el archivo JSON
    json_data = cargar_json(nombre_archivo)
    # Solicitamos al usuario que ingrese un deporte
    deporte_ingresado = input("Ingrese el deporte: ")
    # Obtenemos los nombres de personas que practican el deporte ingresado
    nombres_deporte = obtener_nombres_por_deporte(json_data, deporte_ingresado)
    # Imprimimos los nombres de personas que practican el deporte ingresado
    print("Nombres completos de personas que practican", deporte_ingresado + ":")
    for nombre in nombres_deporte:
        print("- " + nombre)
    # Solicitamos al usuario que ingrese un rango de edades
    edad_minima = int(input("Ingrese la edad mínima: "))
    edad_maxima = int(input("Ingrese la edad máxima: "))
    # Obtenemos los nombres de personas en el rango de edades especificado
    nombres_rango_edad = obtener_nombres_por_rango_edad(json_data, edad_minima, edad_maxima)
    # Imprimimos los nombres de personas en el rango de edades especificado
    print("Nombres completos de personas en el rango de edades", edad_minima, "a", edad_maxima + ":")
    for nombre in nombres_rango_edad:
        print("- " + nombre)
