from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "cancha-reserva-secret"

    from app.controllers.reserva_controller import reserva_bp
    app.register_blueprint(reserva_bp)

    return app
