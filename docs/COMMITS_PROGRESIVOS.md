# Commits progresivos

Este documento separa la historia de commits y describe cada etapa de desarrollo del proyecto CanchaReserva.

## Objetivo

Tener una guía clara de los mensajes de commit usados para cada avance específico del proyecto.

## Mensajes de commit y descripción

1. `Crear estructura inicial del proyecto`
   - Se creó la app Flask y la configuración básica en `run.py`.
   - Se estableció la estructura MVC con carpetas `app/models`, `app/views`, `app/controllers`, `app/services`.

2. `Agregar modelo Cancha`
   - Se añadió el modelo `Cancha` en `app/models/cancha.py`.
   - Define atributos como nombre, tipo de cancha y precio por hora.

3. `Agregar modelo Reserva`
   - Se añadió el modelo `Reserva` en `app/models/reserva.py`.
   - Define fecha, hora, duración y referencia a la cancha reservada.

4. `Crear servicio de reservas`
   - Se implementó `app/services/reserva_service.py`.
   - Incluye lógica para crear, validar, buscar y cancelar reservas.

5. `Crear controlador principal`
   - Se añadió `app/controllers/reserva_controller.py`.
   - Maneja rutas para reservar, consultar disponibilidad y listar reservas.

6. `Crear vista de inicio`
   - Se creó `app/templates/index.html`.
   - Define la página principal y la navegación del sistema.

7. `Crear formulario de reserva`
   - Se creó `app/templates/reservar.html`.
   - Incluye campos para cancha, fecha, hora y duración.

8. `Mostrar lista de reservas`
   - Se creó `app/templates/reservas.html`.
   - Muestra las reservas guardadas en memoria.

9. `Agregar validaciones y lógica de precio`
   - Se mejoraron las validaciones de disponibilidad.
   - Se agregó el cálculo de precio según tipo de cancha y duración.

10. `Organizar documentación en docs/`
    - Se movieron los archivos de soporte a la carpeta `docs/`.
    - Se creó documentación adicional de desarrollo y defensa técnica.

11. `Añadir .gitignore y scripts de inicio`
    - Se añadió `.gitignore`.
    - Se movió `INICIAR_APP.bat` a `scripts/`.

12. `Refinar estilo y ajustes finales`
    - Se realizaron mejoras visuales y correcciones menores.
    - Se actualizó la documentación con un enfoque iterativo y específico.
