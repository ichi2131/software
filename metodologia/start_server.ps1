# Script para iniciar el servidor del Sistema de Administración de Inventario
# Uso: .\start_server.ps1

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Error: Python no se encuentra en el PATH" -ForegroundColor Red
    Write-Host "Por favor instala Python desde: https://www.python.org" -ForegroundColor Yellow
    Read-Host "Presiona ENTER para salir"
    exit 1
}

# Cambiar al directorio del script
Set-Location $PSScriptRoot

# Limpiar pantalla
Clear-Host

# Mostrar información
Write-Host "" -NoNewline
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "    SISTEMA DE ADMINISTRACION DE INVENTARIO" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Mostrar instrucciones
Write-Host "📍 Directorio: " -NoNewline
Write-Host (Get-Location) -ForegroundColor Yellow

Write-Host "🌐 Servidor: " -NoNewline
Write-Host "http://localhost:8000" -ForegroundColor Green

Write-Host ""
Write-Host "Usuarios de prueba:" -ForegroundColor Magenta
Write-Host "  • Owner:      owner / owner123" -ForegroundColor White
Write-Host "  • Admin:      admin / admin123" -ForegroundColor White
Write-Host "  • Inspector:  tester / tester123" -ForegroundColor White
Write-Host "  • Tesorera:   tesorera / tesorera123" -ForegroundColor White
Write-Host "  • Comprador:  buyer / buyer123" -ForegroundColor White

Write-Host ""
Write-Host "⏹️  Presiona CTRL+C para detener el servidor" -ForegroundColor Yellow
Write-Host ""

# Ejecutar el servidor
try {
    python server.py
} catch {
    Write-Host "Error al ejecutar el servidor: $_" -ForegroundColor Red
    Read-Host "Presiona ENTER para salir"
    exit 1
}
