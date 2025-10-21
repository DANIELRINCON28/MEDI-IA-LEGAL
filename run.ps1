# Script de ejecución rápida para Windows PowerShell
# MEDI-IA-LEGAL Run Script

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  MEDI-IA-LEGAL - Iniciando Sistema" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si el entorno virtual existe
if (-not (Test-Path "venv")) {
    Write-Host "✗ Entorno virtual no encontrado." -ForegroundColor Red
    Write-Host "  Ejecuta primero: .\setup.ps1" -ForegroundColor Yellow
    exit 1
}

# Activar entorno virtual
Write-Host "Activando entorno virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Verificar API key
$envContent = Get-Content .env -Raw -ErrorAction SilentlyContinue
if ($envContent -match 'GROQ_API_KEY="tu_api_key_de_groq"' -or -not $envContent) {
    Write-Host ""
    Write-Host "⚠ ADVERTENCIA: GROQ_API_KEY no está configurada" -ForegroundColor Yellow
    Write-Host "  La aplicación puede fallar sin una API key válida." -ForegroundColor Yellow
    Write-Host "  Configúrala en el archivo .env antes de continuar." -ForegroundColor Yellow
    Write-Host ""
    $continue = Read-Host "¿Deseas continuar de todos modos? (s/n)"
    if ($continue -ne "s") {
        exit 0
    }
}

# Ejecutar Streamlit
Write-Host ""
Write-Host "Iniciando MEDI-IA-LEGAL..." -ForegroundColor Green
Write-Host "La aplicación se abrirá en tu navegador." -ForegroundColor Cyan
Write-Host "Presiona Ctrl+C para detener el servidor." -ForegroundColor Yellow
Write-Host ""

streamlit run app.py
