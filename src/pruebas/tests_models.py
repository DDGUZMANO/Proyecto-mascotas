from src.modelos.models import Usuario, Cuidador, Mascota

def test_creacion_modelos():
    usuario1 = Usuario(id_usuario=1, nombre="Ana", ubicacion="Madrid", tipo_mascota_preferida="Perro")
    cuidador1 = Cuidador(id_cuidador=101, nombre="Carlos", ubicacion="Madrid", tipo_mascota_aceptada="Perro", tamaño_mascota_aceptada="Grande", experiencia=5)
    mascota1 = Mascota(id_mascota=1001, nombre="Max", tipo_mascota="Perro", tamaño="Grande", necesidades_especiales=False, id_usuario=1)
    assert usuario1.nombre == "Ana"
    assert cuidador1.experiencia == 5
    assert mascota1.tipo_mascota == "Perro"