# CanchaReserva

Aplicación web sencilla con patrón MVC para gestionar reservas de canchas deportivas.

## Funciones
- Registrar reservas.
- Ver reservas creadas.
- Consultar disponibilidad por fecha, hora y tipo de cancha.
- Cancelar reservas.
- Calcular precio según tipo de cancha y duración.
- Validaciones básicas.
- Proyecto organizado por MVC.
- Incluye guía de commits y evidencia de prompting.

## Tecnologías
- Python
- Flask
- HTML
- CSS
- Almacenamiento en memoria

## Cómo ejecutar en VS Code

1. Abre la carpeta del proyecto.
2. Abre una terminal.
3. Crea un entorno virtual:

```bash
python -m venv .venv
```

4. Activa el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Si PowerShell bloquea la activación, usa:

```bash
.venv\Scripts\Activate.ps1
```

o ejecuta:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

5. Instala Flask:

```bash
pip install -r requirements.txt
```

6. Ejecuta la aplicación:

```bash
python run.py
```

7. Abre en el navegador:

```text
http://127.0.0.1:5000
```

## Estructura MVC

- Modelo: `app/models/`
- Vista: `app/templates/`
- Controlador: `app/controllers/`
- Servicio/lógica: `app/services/`

## Commits sugeridos

1. Crear estructura inicial del proyecto.
2. Agregar modelo Cancha.
3. Agregar modelo Reserva.
4. Crear servicio de reservas.
5. Crear controlador principal.
6. Crear vista de inicio.
7. Crear formulario de reserva.
8. Mostrar lista de reservas.
9. Agregar cancelación de reservas.
10. Agregar validaciones y cálculo de precio.
11. Mejorar estilos visuales.
12. Agregar documentación y prompts usados.
