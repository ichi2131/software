@echo off
REM Script para iniciar el Sistema de Administración de Inventario con API

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║  Sistema de Administración de Inventario - Inicializador   ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Obtener directorio actual
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"
echo Directorio: %SCRIPT_DIR%
echo.

REM Verificar Python
echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    pause
    exit /b 1
)

REM Instalar dependencias
echo.
echo Instalando dependencias...
python -m pip install -q -r requirements.txt
if errorlevel 1 (
    echo ADVERTENCIA: Hubo un problema al instalar las dependencias
    echo Intenta manualmente: python -m pip install -r requirements.txt
)

REM Iniciar API
echo.
echo ═══════════════════════════════════════════════════════════
echo Iniciando la API...
echo La API estará disponible en: http://localhost:5000
echo ═══════════════════════════════════════════════════════════
echo.

REM Ejecutar API
python api.py

REM Si llegamos aquí, la API se cerró
echo.
echo API detenida.
pause
