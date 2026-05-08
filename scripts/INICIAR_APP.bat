@echo off
title CanchaReserva

echo ==========================================
echo      INICIANDO CANCHARESERVA APP
echo ==========================================
echo.

IF NOT EXIST .venv (
    echo Creando entorno virtual...
    python -m venv .venv
)

call .venv\Scripts\activate

echo.
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo ==========================================
echo  APP EJECUTANDO EN:
echo  http://127.0.0.1:5000
echo ==========================================
echo.

python run.py

pause
