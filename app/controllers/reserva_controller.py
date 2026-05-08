from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.reserva_service import reserva_service

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/")
def inicio():
    return render_template("index.html", canchas=reserva_service.listar_canchas())

@reserva_bp.route("/reservar", methods=["GET", "POST"])
def reservar():
    if request.method == "POST":
        cliente = request.form.get("cliente", "")
        telefono = request.form.get("telefono", "")
        cancha_id = int(request.form.get("cancha_id", 0))
        fecha = request.form.get("fecha", "")
        hora = request.form.get("hora", "")
        duracion = int(request.form.get("duracion", 1))

        reserva, mensaje = reserva_service.crear_reserva(
            cliente, telefono, cancha_id, fecha, hora, duracion
        )

        if reserva:
            flash(mensaje, "success")
            return redirect(url_for("reserva.reservas"))

        flash(mensaje, "error")

    return render_template("reservar.html", canchas=reserva_service.listar_canchas())

@reserva_bp.route("/reservas")
def reservas():
    return render_template("reservas.html", reservas=reserva_service.listar_reservas())

@reserva_bp.route("/cancelar/<int:reserva_id>")
def cancelar(reserva_id):
    reserva_service.cancelar_reserva(reserva_id)
    flash("Reserva cancelada correctamente.", "success")
    return redirect(url_for("reserva.reservas"))

@reserva_bp.route("/disponibilidad", methods=["GET", "POST"])
def disponibilidad():
    resultado = None

    if request.method == "POST":
        cancha_id = int(request.form.get("cancha_id", 0))
        fecha = request.form.get("fecha", "")
        hora = request.form.get("hora", "")

        disponible = reserva_service.esta_disponible(cancha_id, fecha, hora)
        cancha = reserva_service.buscar_cancha(cancha_id)

        resultado = {
            "disponible": disponible,
            "cancha": cancha,
            "fecha": fecha,
            "hora": hora
        }

    return render_template(
        "disponibilidad.html",
        canchas=reserva_service.listar_canchas(),
        resultado=resultado
    )
