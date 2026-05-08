# Evidencia de Prompting

Este documento documenta los prompts utilizados para guiar la construcción iterativa del proyecto y el contexto en cada etapa.

## Prompt 1: Idea del proyecto
"Diseña una aplicación web sencilla con patrón MVC para gestionar reservas de canchas deportivas, fácil de defender en clase."

- Resultado: definición del alcance, tecnología y estructura base del proyecto.

## Prompt 2: Modelo de datos
"Crea los modelos necesarios para una app de reservas de canchas: cliente, cancha y reserva."

- Resultado: creación de los modelos `Cancha` y `Reserva`, con atributos para fecha, hora, duración y tipo de cancha.
- Nota: se optó por mantener el almacenamiento en memoria en este prototipo.

## Prompt 3: Validaciones
"Propón validaciones básicas para evitar reservas duplicadas en la misma fecha, hora y cancha."

- Resultado: lógica de comprobación de disponibilidad antes de crear una reserva.
- Se agregó control de colisiones de horario y validación de campos obligatorios.

## Prompt 4: Interfaz
"Diseña una interfaz sencilla y moderna para una app de reservas deportivas."

- Resultado: vistas de inicio, reserva, disponibilidad y lista de reservas.
- Se usaron plantillas HTML limpias y CSS básico para facilitar la navegación.

## Prompt 5: Defensa técnica
"Explícame cómo defender una aplicación MVC de reservas de canchas en una exposición de 10 minutos."

- Resultado: se generó la estructura de defensa técnica basada en arquitectura, iteraciones y decisiones no genéricas.
- Se documentó en `docs/DEFENSA_TECNICA.md`.

## Prompt 6: Commits
"Dame una lista de commits progresivos para evidenciar el desarrollo por etapas de una aplicación web."

- Resultado: lista de commits con mensajes descriptivos y transferencia a la documentación.
- Se siguió un enfoque de desarrollo por etapas: estructura, modelo, servicio, controlador, vista y documentación.

## Contexto de construcción iterativa

Cada prompt no fue genérico, sino que se usó para agregar una parte concreta del sistema:

- prompt 1 definió el proyecto y la estructura base.
- prompt 2 ayudó a modelar datos concretos.
- prompt 3 mejoró la lógica del negocio.
- prompt 4 construyó la interfaz de usuario.
- prompt 5 llevó a la defensa técnica.
- prompt 6 guió los commits por etapas.

Esto garantiza que el proyecto se construyó con un propósito y una evolución clara, no como un ejemplo abstracto.
