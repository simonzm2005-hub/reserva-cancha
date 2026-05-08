# Defensa técnica

Este proyecto se construyó de forma iterativa sobre un contexto real proporcionado en prompts, con un enfoque no genérico y adaptado a las necesidades de una aplicación de reservas de canchas deportivas.

## Contexto y objetivo

- Requerimiento principal: una aplicación web que permita reservar canchas, consultar disponibilidad y administrar reservas.
- Arquitectura: patrón MVC con separación clara entre modelos, vistas, controladores y lógica de negocio.
- Alcance: interfaz básica, almacenamiento en memoria, validaciones de horario y cálculo de precio.
- Prompts usados: el desarrollo se basó en instrucciones paso a paso para definir modelo, validaciones, UI, commits y documentación.

## Construcción iterativa

El proyecto no se realizó de una sola vez. Se construyó en etapas claras:

1. Estructura inicial del proyecto.
   - Crear la app Flask y la base del MVC.
   - Definir rutas principales y la carpeta de templates.

2. Modelado de datos.
   - Agregar `Cancha` con atributos como tipo y precio.
   - Agregar `Reserva` con fecha, hora, duración y referencia a cancha.

3. Servicio de reservas.
   - Implementar lógica para crear, validar y cancelar reservas.
   - Evitar reservas duplicadas en el mismo horario.
   - Calcular precio según tipo de cancha y duración.

4. Controlador y vistas.
   - Crear formulario de reserva.
   - Generar vista de disponibilidad.
   - Mostrar lista de reservas activas.

5. Documentación y limpieza.
   - Organizar archivos en `docs/` y `scripts/`.
   - Añadir `.gitignore` y mensajes de commit descriptivos.

## Decisiones técnicas clave

- MVC seleccionado para separar presentación, datos y lógica.
- La información se guarda en memoria para simplificar el prototipo y enfocarse en el flujo funcional.
- Se usó Flask 3 y HTML/CSS sencillos para asegurar compatibilidad y claridad.
- Se evitó crear una solución genérica; cada prompt generó una mejora real y concreta en el sistema.

## Componentes del sistema

### Modelo
- `app/models/cancha.py`
- `app/models/reserva.py`

### Servicio
- `app/services/reserva_service.py`

### Controlador
- `app/controllers/reserva_controller.py`

### Vistas
- `app/templates/index.html`
- `app/templates/disponibilidad.html`
- `app/templates/reservar.html`
- `app/templates/reservas.html`

## Cómo defenderlo

1. Explicar el contexto de los prompts: idea, modelo, validaciones, UI y commits.
2. Mostrar la estructura MVC como base de mantenimiento y escalabilidad.
3. Resaltar la construcción iterativa: cada etapa resolvió una necesidad específica.
4. Señalar que no es una plantilla genérica; se implementaron requisitos concretos: disponibilidad, reserva y cálculo de precio.
5. Mencionar que el prototipo puede crecer hacia persistencia real (base de datos) y autenticación.
