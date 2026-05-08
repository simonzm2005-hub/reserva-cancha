from app.models.cancha import Cancha
from app.models.reserva import Reserva

class ReservaService:
    def __init__(self):
        self.canchas = [
            Cancha(1, "Cancha Norte", "Fútbol 5", 60000),
            Cancha(2, "Cancha Central", "Microfútbol", 50000),
            Cancha(3, "Cancha Arena", "Voleibol", 40000),
            Cancha(4, "Cancha Premium", "Tenis", 45000),
            Cancha(5, "Cancha Urbana", "Baloncesto", 35000),
        ]
        self.reservas = []
        self.contador = 1

    def listar_canchas(self):
        return self.canchas

    def listar_reservas(self):
        return self.reservas

    def buscar_cancha(self, cancha_id):
        return next((c for c in self.canchas if c.id == cancha_id), None)

    def esta_disponible(self, cancha_id, fecha, hora):
        for reserva in self.reservas:
            if (
                reserva.cancha_id == cancha_id
                and reserva.fecha == fecha
                and reserva.hora == hora
                and reserva.estado == "Activa"
            ):
                return False
        return True

    def crear_reserva(self, cliente, telefono, cancha_id, fecha, hora, duracion):
        cancha = self.buscar_cancha(cancha_id)

        if not cancha:
            return None, "La cancha seleccionada no existe."

        if not cliente.strip() or not telefono.strip() or not fecha or not hora:
            return None, "Todos los campos son obligatorios."

        if duracion < 1:
            return None, "La duración debe ser mínimo de 1 hora."

        if not self.esta_disponible(cancha_id, fecha, hora):
            return None, "La cancha ya está reservada en esa fecha y hora."

        total = cancha.precio_hora * duracion

        reserva = Reserva(
            id=self.contador,
            cliente=cliente.strip(),
            telefono=telefono.strip(),
            cancha_id=cancha.id,
            cancha_nombre=f"{cancha.nombre} - {cancha.tipo}",
            fecha=fecha,
            hora=hora,
            duracion=duracion,
            total=total
        )

        self.reservas.append(reserva)
        self.contador += 1

        return reserva, "Reserva creada correctamente."

    def cancelar_reserva(self, reserva_id):
        for reserva in self.reservas:
            if reserva.id == reserva_id:
                reserva.estado = "Cancelada"
                return True
        return False

reserva_service = ReservaService()
