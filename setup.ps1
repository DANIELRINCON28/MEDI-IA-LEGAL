# Script de instalación automática para Windows PowerShell
# MEDI-IA-LEGAL Setup Script

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MEDI-IA-LEGAL - Setup Automático" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
Write-Host "[1/5] Verificando instalación de Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion encontrado" -ForegroundColor Green
} catch {
    Write-Host "✗ Python no está instalado. Por favor, instala Python 3.8+ primero." -ForegroundColor Red
    exit 1
}

# Crear entorno virtual
Write-Host ""
Write-Host "[2/5] Creando entorno virtual..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "⚠ El entorno virtual ya existe. Eliminando..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force venv
}
python -m venv venv
Write-Host "✓ Entorno virtual creado" -ForegroundColor Green

# Activar entorno virtual
Write-Host ""
Write-Host "[3/5] Activando entorno virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✓ Entorno virtual activado" -ForegroundColor Green

# Instalar dependencias
Write-Host ""
Write-Host "[4/5] Instalando dependencias (esto puede tomar unos minutos)..." -ForegroundColor Yellow
pip install --upgrade pip | Out-Null
pip install -r requirements.txt
Write-Host "✓ Dependencias instaladas" -ForegroundColor Green

# Verificar configuración
Write-Host ""
Write-Host "[5/5] Verificando configuración..." -ForegroundColor Yellow

if (Test-Path ".env") {
    $envContent = Get-Content .env -Raw
    if ($envContent -match 'GROQ_API_KEY="tu_api_key_de_groq"') {
        Write-Host "⚠ IMPORTANTE: Debes configurar tu GROQ_API_KEY en el archivo .env" -ForegroundColor Yellow
        Write-Host "  1. Obtén tu API key en: https://console.groq.com/" -ForegroundColor Cyan
        Write-Host "  2. Edita el archivo .env y reemplaza 'tu_api_key_de_groq' con tu key real" -ForegroundColor Cyan
    } else {
        Write-Host "✓ Archivo .env configurado" -ForegroundColor Green
    }
} else {
    Write-Host "✗ Archivo .env no encontrado" -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ✓ Instalación completada" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para ejecutar la aplicación:" -ForegroundColor Yellow
Write-Host "  1. Asegúrate de que el entorno virtual esté activado" -ForegroundColor White
Write-Host "  2. Configura tu GROQ_API_KEY en .env" -ForegroundColor White
Write-Host "  3. Ejecuta: streamlit run app.py" -ForegroundColor White
Write-Host ""
