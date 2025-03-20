def calcular_compatibilidad_mascota(mascota, cuidador):
    """
    Calcula la compatibilidad entre una mascota y un cuidador.

    Args:
        mascota (dict): Diccionario con los datos de la mascota.
        cuidador (dict): Diccionario con los datos del cuidador.

    Returns:
        int: Puntuación de compatibilidad.
    """
    compatibilidad_mascota = 0

    # Comprobar tipo de animal
    if mascota['tipo_animal_Perro'] == 1 and cuidador['acepta_Perro'] == 1:
        compatibilidad_mascota += 1
    if mascota['tipo_animal_Gato'] == 1 and cuidador['acepta_Gato'] == 1:
        compatibilidad_mascota += 1
    if mascota['tipo_animal_Ave'] == 1 and cuidador['acepta_Ave'] == 1:
        compatibilidad_mascota += 1
    if mascota['tipo_animal_Roedor'] == 1 and cuidador['acepta_Roedor'] == 1:
        compatibilidad_mascota += 1

    # Comprobar ubicación (barrio)
    # Asumiendo que tienes una lista de nombres de columnas de ubicación
    ubicaciones = [col for col in cuidador if col.startswith('ubicacion_')]
    for ubicacion in ubicaciones:
        if mascota[ubicacion] == 1 and cuidador[ubicacion] == 1:
            compatibilidad_mascota += 1

    # Comprobar tamaño de mascota
    if mascota['tamanio_Pequeño'] == 1 and cuidador['tamaño_mascota_aceptada_Pequeño'] == 1:
        compatibilidad_mascota += 1
    if mascota['tamanio_Grande'] == 1 and cuidador['tamaño_mascota_aceptada_Grande'] == 1:
        compatibilidad_mascota += 1

    # Comprobar necesidades especiales y experiencia
    if mascota['necesidades_especiales_True'] == 1:
        if cuidador['experiencia'] > 5:
            compatibilidad_mascota += 1
        else:
            compatibilidad_mascota -= 1  # Penalizar la incompatibilidad

    return compatibilidad_mascota


def encontrar_compatibles_mascota(datos_formulario, tipo_usuario, base_de_datos):
    """
    Encuentra cuidadores o mascotas compatibles con los datos del formulario.

    Args:
        datos_formulario (dict): Diccionario con los datos del formulario.
        tipo_usuario (str): "mascota" o "cuidador".
        base_de_datos (list): Lista de diccionarios con los datos de la base de datos.

    Returns:
        list: Lista de tuplas (compatibilidad, id_usuario).
    """

    resultados_mascota = []
    for usuario in base_de_datos:
        if tipo_usuario == "mascota":
            compatibilidad = calcular_compatibilidad_mascota(datos_formulario, usuario)
            resultados_mascota.append((compatibilidad, usuario["id"]))
        elif tipo_usuario == "cuidador":
            compatibilidad = calcular_compatibilidad_mascota(usuario, datos_formulario)
            resultados_mascota.append((compatibilidad, usuario["id"]))

    resultados_mascota.sort(key=lambda x: x[0], reverse=True)
    return resultados_mascota


def generar_salida_usuario_cuidador(resultados, base_de_datos_cuidadores, num_cuidadores=2):
    """
    Genera una lista de diccionarios con la información de los cuidadores más compatibles.

    Args:
        resultados (list): Lista de tuplas (compatibilidad, id_cuidador).
        base_de_datos_cuidadores (list): Lista de diccionarios con los datos de los cuidadores.
        num_cuidadores (int): Número de cuidadores a mostrar (por defecto, 2).

    Returns:
        list: Lista de diccionarios con la información de los cuidadores.
    """

    salida_usuario_cuidador = []
    for compatibilidad, id_cuidador in resultados[:num_cuidadores]:  # Toma solo los primeros num_cuidadores
        for cuidador in base_de_datos_cuidadores:
            if cuidador["id"] == id_cuidador:
                salida_usuario_cuidador.append(
                    {
                        "id": cuidador["id"],
                        "nombre": cuidador["nombre"],
                        "compatibilidad": compatibilidad,
                        # Agrega aquí otros datos del cuidador que quieras mostrar
                    }
                )
                break  # Encontró el cuidador, no necesita seguir buscando
    return salida_usuario_cuidador