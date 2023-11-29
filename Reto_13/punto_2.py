def mezclar(dic1, dic2):
    # Crear un nuevo diccionario inicialmente vacío
    diccionario_mezclado = {}
    # Agregar las llaves y valores del primer diccionario al diccionario mezclado
    for clave, valor in dic1.items():
        diccionario_mezclado[clave] = valor
    # Agregar las llaves y valores del segundo diccionario al diccionario mezclado,
    # solo si la clave no existe en el diccionario mezclado
    for clave, valor in dic2.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
    # Devolver el diccionario mezclado
    return diccionario_mezclado
# Ejemplo de uso
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'd': 5, 'e': 6}
# Llamar a la función con los dos diccionarios como argumentos
resultado = mezclar(diccionario1, diccionario2)
# Imprimir el resultado
print(resultado)