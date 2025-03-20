def calcular_compatibilidad_cuidador(cuidador, mascota):
    """
    Calcula la compatibilidad de un cuidador con una mascota.

    Args:
        cuidador (dict): Diccionario con los datos del cuidador.
        mascota (dict): Diccionario con los datos de la mascota.

    Returns:
        int: Puntuación de compatibilidad.
    """
    compatibilidad_cuidador = 0

    # Comprobar tipo de mascota
    if cuidador['acepta_Perro'] == 1 and mascota['tipo_animal_Perro'] == 1:
        compatibilidad_cuidador += 1
    if cuidador['acepta_Gato'] == 1 and mascota['tipo_animal_Gato'] == 1:
        compatibilidad_cuidador += 1
    if cuidador['acepta_Ave'] == 1 and mascota['tipo_animal_Ave'] == 1:
        compatibilidad_cuidador += 1
    if cuidador['acepta_Roedor'] == 1 and mascota['tipo_animal_Roedor'] == 1:
        compatibilidad_cuidador += 1

    # Comprobar ubicación (barrio)
    for ubicacion in cuidador:
        if "ubicacion_" in ubicacion:
            if cuidador[ubicacion] == 1 and mascota[ubicacion] == 1:
                compatibilidad_cuidador += 1

    # Comprobar tamaño de mascota
    if cuidador['tamaño_mascota_aceptada_Pequeño'] == 1 and mascota['tamanio_Pequeño'] == 1:
        compatibilidad_cuidador += 1
    if cuidador['tamaño_mascota_aceptada_Grande'] == 1 and mascota['tamanio_Grande'] == 1:
        compatibilidad_cuidador += 1

    # Comprobar necesidades especiales y experiencia (si aplica)
    if 'necesidades_especiales_True' in mascota:
        if mascota['necesidades_especiales_True'] == 1:
            if cuidador['experiencia'] > 5:
                compatibilidad_cuidador += 1
            else:
                compatibilidad_cuidador -= 1  # Penalizar la incompatibilidad

    return compatibilidad_cuidador



def encontrar_compatibles_cuidador(datos_formulario, base_de_datos_mascotas):
    """
    Encuentra mascotas compatibles con los datos del cuidador.

    Args:
        datos_formulario (dict): Diccionario con los datos del cuidador.
        base_de_datos_mascotas (list): Lista de diccionarios con los datos de las mascotas.

    Returns:
        list: Lista de tuplas (compatibilidad, id_mascota).
    """

    resultados_cuidador = []
    for mascota in base_de_datos_mascotas:
        compatibilidad = calcular_compatibilidad_cuidador(datos_formulario, mascota)
        resultados_cuidador.append((compatibilidad, mascota["id"]))  # Asumiendo que cada mascota tiene un "id"

    resultados_cuidador.sort(key=lambda x: x[0], reverse=True)
    return resultados_cuidador


def generar_salida_usuario_mascotas(resultados_cuidador, base_de_datos_mascotas, num_mascotas=2):
    salida_usuario_mascotas = []
    for compatibilidad_cuidador, id_mascota in resultados_cuidador[:num_mascotas]:
        for mascota in base_de_datos_mascotas:
            if mascota["id"] == id_mascota:
                salida_usuario_mascotas.append(
                    {
                        "id": mascota["id"],
                        "nombre": mascota["nombre"],
                        "compatibilidad": compatibilidad_cuidador,
                        "url_imagen": mascota["url_imagen"],
                    }
                )
                break
    return salida_usuario_mascotas