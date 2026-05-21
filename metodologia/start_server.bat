@echo off
REM Inicia el servidor HTTP del Sistema de Administración de Inventario
REM Este script ejecuta automáticamente los gráficos y abre la aplicación

setlocal enabledelayedexpansion

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo =====================================
    echo ERROR: Python no encontrado
    echo =====================================
    echo.
    echo Python no está instalado o no se encuentra en el PATH
    echo Por favor instala Python desde: https://www.python.org
    echo.
    pause
    exit /b 1
)

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Limpiar pantalla
cls

REM Mostrar banner
echo.
echo ============================================================
echo    SISTEMA DE ADMINISTRACION DE INVENTARIO
echo ============================================================
echo.
echo Iniciando servidor...
echo.

REM Iniciar el servidor Python
python server.py

REM Si llegamos aquí, el servidor se cerró
echo.
echo ============================================================
echo Servidor detenido
echo ============================================================
pause
