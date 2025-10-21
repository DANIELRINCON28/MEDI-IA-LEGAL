# ⚡ COMANDOS RÁPIDOS - MEDI-IA-LEGAL

## 🚀 INICIO RÁPIDO

### Opción 1: Automático (Windows)
```powershell
.\setup.ps1    # Instalación completa
.\run.ps1      # Ejecutar aplicación
```

### Opción 2: Manual
```powershell
# Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app.py
```

---

## 🔧 COMANDOS DE DESARROLLO

### Gestión del Entorno Virtual

**Crear:**
```powershell
python -m venv venv
```

**Activar:**
```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

**Desactivar:**
```powershell
deactivate
```

**Eliminar:**
```powershell
# Windows
Remove-Item -Recurse -Force venv

# macOS/Linux
rm -rf venv
```

---

## 📦 GESTIÓN DE DEPENDENCIAS

**Instalar todas:**
```bash
pip install -r requirements.txt
```

**Instalar una específica:**
```bash
pip install langchain
pip install streamlit
pip install langgraph
```

**Actualizar pip:**
```bash
python -m pip install --upgrade pip
```

**Ver instaladas:**
```bash
pip list
pip list | grep -E "langchain|streamlit"
```

**Generar requirements.txt:**
```bash
pip freeze > requirements.txt
```

---

## 🧪 TESTING Y VERIFICACIÓN

**Test de configuración:**
```bash
python test_setup.py
```

**Verificar Python:**
```bash
python --version
python -c "import sys; print(sys.version)"
```

**Verificar imports:**
```bash
python -c "import langchain; print('✓ LangChain')"
python -c "import langgraph; print('✓ LangGraph')"
python -c "import streamlit; print('✓ Streamlit')"
```

**Verificar archivos:**
```powershell
# Windows PowerShell
Get-ChildItem -Recurse -File | Select-Object Name, Length

# macOS/Linux
find . -type f -name "*.py" | wc -l
```

---

## 🎯 EJECUCIÓN

**Ejecutar Streamlit:**
```bash
streamlit run app.py
```

**Con puerto específico:**
```bash
streamlit run app.py --server.port 8502
```

**Sin abrir navegador:**
```bash
streamlit run app.py --server.headless true
```

**Ver ayuda de Streamlit:**
```bash
streamlit --help
streamlit run --help
```

---

## 📊 MONITOREO Y LOGS

**Ver versión de Streamlit:**
```bash
streamlit version
```

**Ver configuración:**
```bash
streamlit config show
```

**Cache de Streamlit:**
```bash
# Limpiar cache
streamlit cache clear
```

---

## 🔍 DEBUGGING

**Ejecutar Python en modo verbose:**
```bash
python -v test_setup.py
```

**Ver variables de entorno:**
```powershell
# Windows PowerShell
Get-Content .env

# macOS/Linux
cat .env
```

**Verificar API key (sin mostrarla):**
```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓ Key loaded' if os.getenv('GROQ_API_KEY') else '✗ Key missing')"
```

**Test rápido de herramientas:**
```bash
python -c "from tools import calculate_society_split; print(calculate_society_split(500, 100))"
```

---

## 📁 GESTIÓN DE ARCHIVOS

**Listar estructura:**
```powershell
# Windows PowerShell
tree /F

# macOS/Linux
tree
```

**Contar líneas de código:**
```powershell
# Windows PowerShell
(Get-Content *.py | Measure-Object -Line).Lines

# macOS/Linux
wc -l *.py
```

**Buscar en archivos:**
```powershell
# Windows PowerShell
Select-String -Path *.py -Pattern "def "

# macOS/Linux
grep -r "def " *.py
```

---

## 🔄 GIT (si usas control de versiones)

**Inicializar repositorio:**
```bash
git init
git add .
git commit -m "Initial commit: MEDI-IA-LEGAL prototype"
```

**Ver estado:**
```bash
git status
```

**Ver cambios:**
```bash
git diff
```

**Crear rama para demo:**
```bash
git checkout -b demo
```

---

## 🧹 LIMPIEZA

**Eliminar cache de Python:**
```powershell
# Windows PowerShell
Remove-Item -Recurse -Force __pycache__
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force

# macOS/Linux
find . -type d -name "__pycache__" -exec rm -rf {} +
```

**Eliminar archivos temporales:**
```powershell
# Windows PowerShell
Remove-Item *.pyc, *.pyo

# macOS/Linux
find . -name "*.pyc" -delete
find . -name "*.pyo" -delete
```

---

## 🔐 SEGURIDAD

**Verificar que .env NO está en Git:**
```bash
git check-ignore .env
# Debe devolver: .env
```

**Generar .env de ejemplo:**
```bash
# Windows PowerShell
Get-Content .env | ForEach-Object { $_ -replace 'gsk_.*', 'tu_api_key_aqui' } > .env.example

# macOS/Linux
sed 's/gsk_.*/tu_api_key_aqui/' .env > .env.example
```

---

## 📊 INFORMACIÓN DEL SISTEMA

**Info de Python:**
```bash
python -c "import sys; print(f'Python: {sys.version}\nPath: {sys.executable}')"
```

**Info de memoria:**
```bash
python -c "import psutil; print(f'RAM: {psutil.virtual_memory().percent}%')"
```

**Info del proyecto:**
```bash
python -c "import os; print(f'Directorio: {os.getcwd()}\nArchivos: {len(os.listdir())}')"
```

---

## 🚨 COMANDOS DE EMERGENCIA

**Reinstalación completa:**
```powershell
# 1. Eliminar entorno
Remove-Item -Recurse -Force venv

# 2. Recrear
python -m venv venv

# 3. Activar
.\venv\Scripts\activate

# 4. Actualizar pip
python -m pip install --upgrade pip

# 5. Reinstalar
pip install -r requirements.txt
```

**Forzar reinstalación de dependencias:**
```bash
pip install --force-reinstall -r requirements.txt
```

**Instalar desde cache:**
```bash
pip install --no-cache-dir -r requirements.txt
```

---

## 📝 COMANDOS ÚTILES PARA LA DEMO

**Abrir múltiples terminales:**
```powershell
# Terminal 1: Streamlit
streamlit run app.py

# Terminal 2: Monitoreo
python test_setup.py
```

**Copiar contenido de archivo:**
```powershell
# Windows PowerShell
Get-Content EXAMPLES.md | Set-Clipboard

# macOS
pbcopy < EXAMPLES.md

# Linux
xclip -sel clip < EXAMPLES.md
```

---

## 🎬 CHECKLIST PRE-DEMO (comandos)

```powershell
# 1. Activar entorno
.\venv\Scripts\activate

# 2. Verificar setup
python test_setup.py

# 3. Verificar API key
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✓' if os.getenv('GROQ_API_KEY') else '✗')"

# 4. Ejecutar app
streamlit run app.py

# 5. En navegador
# http://localhost:8501
```

---

## 💡 TIPS Y TRUCOS

**Reiniciar Streamlit rápido:**
```
Ctrl + C (en terminal)
streamlit run app.py
```

**Ver logs en tiempo real:**
```bash
# Streamlit muestra logs automáticamente en la terminal
```

**Ejecutar sin mostrar warnings:**
```bash
streamlit run app.py --logger.level error
```

**Modo desarrollo (auto-reload):**
```bash
# Streamlit tiene auto-reload por defecto
# Guarda cambios en .py y recarga automáticamente
```

---

## 🔗 URLs ÚTILES

```
Aplicación local:     http://localhost:8501
Groq Console:         https://console.groq.com/
LangGraph Docs:       https://langchain-ai.github.io/langgraph/
LangChain Docs:       https://python.langchain.com/
Streamlit Docs:       https://docs.streamlit.io/
```

---

## 📞 AYUDA RÁPIDA

**Ver ayuda de un comando:**
```bash
python --help
pip --help
streamlit --help
```

**Ver docstring de función:**
```bash
python -c "from tools import calculate_society_split; help(calculate_society_split)"
```

---

## ⌨️ ATAJOS DE TECLADO

**Streamlit:**
- `Ctrl + C`: Detener servidor
- `R` (en browser): Rerun manual
- `C` (en browser): Limpiar cache

**Terminal:**
- `Ctrl + C`: Interrumpir proceso
- `Ctrl + L`: Limpiar pantalla
- `Tab`: Autocompletar

---

*Referencia rápida de comandos para MEDI-IA-LEGAL*
