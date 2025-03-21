from dataclasses import dataclass

@dataclass
class Usuario:
    id_usuario: int
    nombre: str
    ubicacion: str
    tipo_mascota_preferida: str = None 

@dataclass
class Cuidador:
    id_cuidador: int
    nombre: str
    ubicacion: str
    tipo_mascota_aceptada: str
    tamaño_mascota_aceptada: str
    experiencia: int

@dataclass
class Mascota:
    id_mascota: int
    nombre: str
    tipo_mascota: str
    tamaño: str
    necesidades_especiales: bool
    id_usuario: int #Clave foránea que relaciona a la mascota con el usuario