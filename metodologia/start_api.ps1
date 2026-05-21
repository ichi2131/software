#!/usr/bin/env pwsh
<#
Script para iniciar el Sistema de Administración de Inventario con API
Inicia la API Flask y abre el navegador
#>

Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  Sistema de Administración de Inventario - Inicializador   ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "📁 Directorio: $ScriptDir" -ForegroundColor Yellow
Write-Host ""

# Verificar si Python está instalado
Write-Host "🔍 Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python no está instalado o no está en el PATH" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

# Instalar o actualizar dependencias
Write-Host ""
Write-Host "📦 Instalando dependencias..." -ForegroundColor Yellow
Set-Location $ScriptDir
python -m pip install -q -r requirements.txt
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencias instaladas correctamente" -ForegroundColor Green
} else {
    Write-Host "⚠️ Hubo un problema al instalar las dependencias" -ForegroundColor Red
}

# Iniciar la API
Write-Host ""
Write-Host "🚀 Iniciando la API..." -ForegroundColor Yellow
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "💡 La API estará disponible en: http://localhost:5000" -ForegroundColor Cyan
Write-Host "💡 El navegador se abrirá en unos segundos..." -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Ejecutar API en background y obtener el PID
$apiProcess = Start-Process python -ArgumentList "api.py" -PassThru -NoNewWindow

# Esperar un poco para que la API se inicie
Start-Sleep -Seconds 3

# Verificar que la API está corriendo
$apiRunning = Get-Process -Id $apiProcess.Id -ErrorAction SilentlyContinue
if ($apiRunning) {
    Write-Host "✅ API iniciada correctamente (PID: $($apiProcess.Id))" -ForegroundColor Green
    
    # Abrir el navegador
    Write-Host ""
    Write-Host "🌐 Abriendo navegador..." -ForegroundColor Yellow
    Start-Sleep -Seconds 1
    Start-Process "http://localhost:8000/login.html"
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "✨ Sistema iniciado correctamente" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📋 Credenciales de prueba:" -ForegroundColor Yellow
    Write-Host "  Owner:     owner / owner123" -ForegroundColor White
    Write-Host "  Admin:     admin / admin123" -ForegroundColor White
    Write-Host "  Inspector: tester / tester123" -ForegroundColor White
    Write-Host "  Tesorera:  tesorera / tesorera123" -ForegroundColor White
    Write-Host "  Comprador: buyer / buyer123" -ForegroundColor White
    Write-Host ""
    Write-Host "⏹️  Para detener la API, cierra esta ventana o presiona Ctrl+C" -ForegroundColor Yellow
    Write-Host ""
    
    # Mantener el proceso activo
    try {
        while ($true) {
            Start-Sleep -Seconds 5
            
            # Verificar que la API sigue corriendo
            $apiRunning = Get-Process -Id $apiProcess.Id -ErrorAction SilentlyContinue
            if (-not $apiRunning) {
                Write-Host ""
                Write-Host "⚠️  La API se ha detenido" -ForegroundColor Yellow
                break
            }
        }
    } catch {
        Write-Host "Deteniendo..."
    } finally {
        # Limpiar
        if ($apiRunning) {
            Stop-Process -Id $apiProcess.Id -Force -ErrorAction SilentlyContinue
        }
        Write-Host "👋 Sistema detenido" -ForegroundColor Cyan
    }
} else {
    Write-Host "❌ No se pudo iniciar la API" -ForegroundColor Red
    Write-Host ""
    Write-Host "Intenta ejecutar manualmente:" -ForegroundColor Yellow
    Write-Host "  python api.py" -ForegroundColor White
    Read-Host "Presiona Enter para salir"
}
