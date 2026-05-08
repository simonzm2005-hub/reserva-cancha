# Defensa técnica corta

El proyecto CanchaReserva es una aplicación web desarrollada con el patrón MVC.

## Modelo
Representa los datos principales del sistema:
- Cancha
- Reserva

## Vista
Son las páginas HTML que ve el usuario:
- Inicio
- Formulario de reserva
- Lista de reservas
- Consulta de disponibilidad

## Controlador
Recibe las peticiones del usuario y decide qué vista mostrar o qué acción ejecutar.

## Servicio
Contiene la lógica del sistema:
- Crear reserva
- Validar disponibilidad
- Cancelar reserva
- Calcular precio

## Explicación rápida
El usuario ingresa al sistema, selecciona una cancha, una fecha, una hora y una duración. El sistema valida que la cancha no esté ocupada en ese horario. Si está disponible, guarda la reserva en memoria y calcula el precio total.
