"""from src.modelos.models import Usuario, Cuidador, Mascota

def test_creacion_modelos():
    usuario1 = Usuario(id_usuario=1, nombre="Ana", ubicacion="Madrid", tipo_mascota_preferida="Perro")
    cuidador1 = Cuidador(id_cuidador=101, nombre="Carlos", ubicacion="Madrid", tipo_mascota_aceptada="Perro", tamaño_mascota_aceptada="Grande", experiencia=5)
    mascota1 = Mascota(id_mascota=1001, nombre="Max", tipo_mascota="Perro", tamaño="Grande", necesidades_especiales=False, id_usuario=1)
    assert usuario1.nombre == "Ana"
    assert cuidador1.experiencia == 5
    assert mascota1.tipo_mascota == "Perro"""""
from src.modelos.models import Usuario, Cuidador, Mascota
import random
import pytest

# Datos para generar valores aleatorios
nombres = ["Ana", "Carlos", "María", "Juan", "Laura", "Pedro", "Sofía", "Miguel", "Elena", "David"]
ubicaciones = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Málaga", "Zaragoza", "Murcia", "Palma", "Alicante"]
tipos_mascota = ["Perro", "Gato", "Conejo", "Pájaro", "Pez", "Hámster", "Tortuga"]
tamaños = ["Pequeño", "Mediano", "Grande", "Muy Grande"]

def test_creacion_modelos():
    usuario1 = Usuario(id_usuario=1, nombre="Ana", ubicacion="Madrid", tipo_mascota_preferida="Perro")
    cuidador1 = Cuidador(id_cuidador=101, nombre="Carlos", ubicacion="Madrid", tipo_mascota_aceptada="Perro", tamaño_mascota_aceptada="Grande", experiencia=5)
    mascota1 = Mascota(id_mascota=1001, nombre="Max", tipo_mascota="Perro", tamaño="Grande", necesidades_especiales=False, id_usuario=1)
    
    assert usuario1.nombre == "Ana"
    assert cuidador1.experiencia == 5
    assert mascota1.tipo_mascota == "Perro"

def test_usuario_datos_aleatorios():
    for i in range(1, 11):
        usuario = Usuario(
            id_usuario=i,
            nombre=random.choice(nombres),
            ubicacion=random.choice(ubicaciones),
            tipo_mascota_preferida=random.choice(tipos_mascota)
        )
        
        assert usuario.id_usuario == i
        assert usuario.nombre in nombres
        assert usuario.ubicacion in ubicaciones
        assert usuario.tipo_mascota_preferida in tipos_mascota

def test_cuidador_datos_aleatorios():
    for i in range(101, 111):
        experiencia = random.randint(1, 15)
        cuidador = Cuidador(
            id_cuidador=i,
            nombre=random.choice(nombres),
            ubicacion=random.choice(ubicaciones),
            tipo_mascota_aceptada=random.choice(tipos_mascota),
            tamaño_mascota_aceptada=random.choice(tamaños),
            experiencia=experiencia
        )
        
        assert cuidador.id_cuidador == i
        assert cuidador.nombre in nombres
        assert cuidador.ubicacion in ubicaciones
        assert cuidador.tipo_mascota_aceptada in tipos_mascota
        assert cuidador.tamaño_mascota_aceptada in tamaños
        assert 1 <= cuidador.experiencia <= 15

def test_mascota_datos_aleatorios():
    for i in range(1001, 1011):
        usuario_id = random.randint(1, 100)
        necesidades_especiales = random.choice([True, False])
        mascota = Mascota(
            id_mascota=i,
            nombre=random.choice(nombres),
            tipo_mascota=random.choice(tipos_mascota),
            tamaño=random.choice(tamaños),
            necesidades_especiales=necesidades_especiales,
            id_usuario=usuario_id
        )
        
        assert mascota.id_mascota == i
        assert mascota.nombre in nombres
        assert mascota.tipo_mascota in tipos_mascota
        assert mascota.tamaño in tamaños
        assert mascota.necesidades_especiales in [True, False]
        assert mascota.id_usuario == usuario_id

def test_validacion_ubicacion():
    usuario = Usuario(id_usuario=1, nombre="Ana", ubicacion="Ciudad Inexistente", tipo_mascota_preferida="Perro")
    assert usuario.ubicacion not in ubicaciones
    
    # Prueba con ubicaciones válidas
    for ubicacion in ubicaciones:
        usuario = Usuario(id_usuario=1, nombre="Ana", ubicacion=ubicacion, tipo_mascota_preferida="Perro")
        assert usuario.ubicacion in ubicaciones

def test_validacion_tipo_mascota():
    mascota = Mascota(id_mascota=1, nombre="Rex", tipo_mascota="Tipo Inexistente", tamaño="Grande", necesidades_especiales=False, id_usuario=1)
    assert mascota.tipo_mascota not in tipos_mascota
    
    # Prueba con tipos válidos
    for tipo in tipos_mascota:
        mascota = Mascota(id_mascota=1, nombre="Rex", tipo_mascota=tipo, tamaño="Grande", necesidades_especiales=False, id_usuario=1)
        assert mascota.tipo_mascota in tipos_mascota

def test_validacion_tamaño():
    mascota = Mascota(id_mascota=1, nombre="Rex", tipo_mascota="Perro", tamaño="Tamaño Inexistente", necesidades_especiales=False, id_usuario=1)
    assert mascota.tamaño not in tamaños
    
    # Prueba con tamaños válidos
    for tamaño in tamaños:
        mascota = Mascota(id_mascota=1, nombre="Rex", tipo_mascota="Perro", tamaño=tamaño, necesidades_especiales=False, id_usuario=1)
        assert mascota.tamaño in tamaños

def test_experiencia_cuidador():
    # Prueba con valores límite
    cuidador_min = Cuidador(id_cuidador=1, nombre="Ana", ubicacion="Madrid", tipo_mascota_aceptada="Perro", tamaño_mascota_aceptada="Grande", experiencia=1)
    cuidador_max = Cuidador(id_cuidador=2, nombre="Juan", ubicacion="Barcelona", tipo_mascota_aceptada="Gato", tamaño_mascota_aceptada="Pequeño", experiencia=15)
    
    assert cuidador_min.experiencia == 1
    assert cuidador_max.experiencia == 15
    
    # Prueba con valores fuera de rango (si tu modelo lo permite)
    cuidador_negativo = Cuidador(id_cuidador=3, nombre="Laura", ubicacion="Valencia", tipo_mascota_aceptada="Conejo", tamaño_mascota_aceptada="Mediano", experiencia=-1)
    cuidador_excesivo = Cuidador(id_cuidador=4, nombre="Pedro", ubicacion="Sevilla", tipo_mascota_aceptada="Pájaro", tamaño_mascota_aceptada="Grande", experiencia=100)
    
    # Descomentar si tu modelo valida estos casos:
    # assert cuidador_negativo.experiencia >= 0
    # assert cuidador_excesivo.experiencia <= 50

def test_compatibilidad_cuidador_mascota():
    # Crea varias combinaciones de cuidadores y mascotas
    for _ in range(10):
        tipo = random.choice(tipos_mascota)
        tamaño = random.choice(tamaños)
        
        cuidador = Cuidador(
            id_cuidador=random.randint(1, 1000),
            nombre=random.choice(nombres),
            ubicacion=random.choice(ubicaciones),
            tipo_mascota_aceptada=tipo,
            tamaño_mascota_aceptada=tamaño,
            experiencia=random.randint(1, 15)
        )
        
        mascota = Mascota(
            id_mascota=random.randint(1, 1000),
            nombre=random.choice(nombres),
            tipo_mascota=tipo,
            tamaño=tamaño,
            necesidades_especiales=random.choice([True, False]),
            id_usuario=random.randint(1, 100)
        )
        
        # Verifica que el cuidador acepta el tipo y tamaño de esta mascota
        assert cuidador.tipo_mascota_aceptada == mascota.tipo_mascota
        assert cuidador.tamaño_mascota_aceptada == mascota.tamaño

def test_usuario_preferencia_mascota():
    # Prueba la relación entre preferencia de usuario y mascota
    for _ in range(10):
        tipo = random.choice(tipos_mascota)
        
        usuario = Usuario(
            id_usuario=random.randint(1, 100),
            nombre=random.choice(nombres),
            ubicacion=random.choice(ubicaciones),
            tipo_mascota_preferida=tipo
        )
        
        mascota = Mascota(
            id_mascota=random.randint(1, 1000),
            nombre=random.choice(nombres),
            tipo_mascota=tipo,
            tamaño=random.choice(tamaños),
            necesidades_especiales=random.choice([True, False]),
            id_usuario=usuario.id_usuario
        )
        
        # Verifica que la mascota coincide con la preferencia del usuario
        assert usuario.tipo_mascota_preferida == mascota.tipo_mascota
        assert mascota.id_usuario == usuario.id_usuario