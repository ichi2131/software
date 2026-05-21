@echo off
REM Script para ejecutar automáticamente el generador de gráficos de inventario
REM Este archivo se ejecutará automáticamente cuando se inicie el sistema

echo.
echo ========================================
echo     Generador de Gráficos de Inventario
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no se encuentra en el PATH
    echo Por favor instala Python desde https://www.python.org
    pause
    exit /b 1
)

REM Ejecutar el script Python
echo Ejecutando generador de gráficos...
python inventory_charts.py

if errorlevel 1 (
    echo.
    echo ERROR: Ocurrió un error al ejecutar el script
    pause
    exit /b 1
)

echo.
echo ✓ Gráficos generados exitosamente
echo.
echo Abriendo archivo de gráficos en navegador...
echo.

REM Intentar abrir el archivo HTML en el navegador predeterminado
start "" "inventory_chart.html"

echo.
echo Proceso completado
pause
