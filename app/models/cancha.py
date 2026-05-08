from dataclasses import dataclass

@dataclass
class Cancha:
    id: int
    nombre: str
    tipo: str
    precio_hora: int
