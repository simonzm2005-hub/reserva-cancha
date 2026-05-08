from dataclasses import dataclass
from datetime import datetime

@dataclass
class Reserva:
    id: int
    cliente: str
    telefono: str
    cancha_id: int
    cancha_nombre: str
    fecha: str
    hora: str
    duracion: int
    total: int
    estado: str = "Activa"

    def fecha_creacion(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")
