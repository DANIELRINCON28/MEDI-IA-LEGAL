# 🚀 INSTRUCCIONES DE INSTALACIÓN PASO A PASO
# MEDI-IA-LEGAL

## OPCIÓN 1: Instalación Automática (Recomendado para Windows)

### Paso 1: Ejecutar el script de instalación
```powershell
.\setup.ps1
```

Si te sale un error de permisos de ejecución, ejecuta primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Paso 2: Configurar tu API Key de Groq

1. Ve a: https://console.groq.com/
2. Crea una cuenta gratuita (o inicia sesión)
3. Ve a "API Keys" en el menú lateral
4. Haz clic en "Create API Key"
5. Copia la key generada (formato: `gsk_...`)
6. Abre el archivo `.env` en tu editor
7. Reemplaza `tu_api_key_de_groq` con tu key real:
   ```
   GROQ_API_KEY="gsk_tu_key_real_aquí"
   ```
8. Guarda el archivo

### Paso 3: Ejecutar la aplicación
```powershell
.\run.ps1
```

¡Listo! La aplicación se abrirá automáticamente en tu navegador.

---

## OPCIÓN 2: Instalación Manual

### Paso 1: Crear el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
```

**macOS/Linux:**
```bash
python3 -m venv venv
```

### Paso 2: Activar el entorno virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

💡 **Nota:** Deberías ver `(venv)` al inicio de tu línea de comando cuando esté activado.

### Paso 3: Actualizar pip
```bash
python -m pip install --upgrade pip
```

### Paso 4: Instalar las dependencias
```bash
pip install -r requirements.txt
```

⏱️ **Tiempo estimado:** 2-5 minutos (depende de tu conexión a internet)

### Paso 5: Configurar la API Key de Groq

**Obtener la API Key:**
1. Visita: https://console.groq.com/
2. Regístrate o inicia sesión
3. Navega a "API Keys"
4. Crea una nueva API key
5. Cópiala (formato: `gsk_...`)

**Configurar en el proyecto:**
1. Abre el archivo `.env`
2. Busca la línea: `GROQ_API_KEY="tu_api_key_de_groq"`
3. Reemplaza `tu_api_key_de_groq` con tu key real
4. Guarda el archivo

**Ejemplo:**
```env
GROQ_API_KEY="gsk_1234567890abcdefghijklmnop"
```

### Paso 6: Verificar la instalación (Opcional pero recomendado)
```bash
python test_setup.py
```

Este script verificará que:
- ✅ Python está correctamente instalado
- ✅ Todas las dependencias están instaladas
- ✅ El archivo .env está configurado
- ✅ Los archivos del corpus existen
- ✅ Las herramientas funcionan correctamente

### Paso 7: Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Problema: "python no se reconoce como un comando..."

**Solución:**
- Python no está instalado o no está en el PATH
- Descarga Python desde: https://www.python.org/downloads/
- Durante la instalación, marca "Add Python to PATH"

---

### Problema: "pip install falla con errores de compilación"

**Solución para Windows:**
```powershell
# Instalar Microsoft C++ Build Tools
# Descarga desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

**Solución para macOS:**
```bash
# Instalar Xcode Command Line Tools
xcode-select --install
```

**Solución para Linux:**
```bash
# Instalar build-essential
sudo apt-get update
sudo apt-get install build-essential
```

---

### Problema: "No module named 'streamlit'"

**Solución:**
```bash
# Asegúrate de que el entorno virtual esté activado
# Deberías ver (venv) al inicio de tu línea de comando

# Si no está activado:
# Windows:
.\venv\Scripts\Activate.ps1

# macOS/Linux:
source venv/bin/activate

# Luego reinstala:
pip install -r requirements.txt
```

---

### Problema: "GROQ_API_KEY not found"

**Solución:**
1. Verifica que el archivo `.env` existe en la raíz del proyecto
2. Abre `.env` y verifica que la línea esté así:
   ```
   GROQ_API_KEY="gsk_tu_key_real"
   ```
3. NO uses comillas simples, solo comillas dobles
4. NO dejes espacios alrededor del `=`
5. Reinicia la aplicación después de modificar `.env`

---

### Problema: "Error loading corpus"

**Solución:**
```bash
# Verifica que la carpeta corpus existe
ls corpus/

# Deberías ver:
# - ley_2442.txt
# - codigo_civil.txt
# - interes_menor.txt

# Si faltan archivos, verifica que se crearon correctamente
# o créalos manualmente según el README.md
```

---

### Problema: "Cannot connect to Groq API"

**Posibles causas:**
1. API Key incorrecta → Verifica tu key en https://console.groq.com/
2. Sin conexión a internet → Verifica tu conexión
3. Firewall/Proxy → Configura excepciones para Python
4. Cuota excedida → Verifica tu uso en el dashboard de Groq

---

### Problema: "Streamlit no abre el navegador automáticamente"

**Solución:**
Abre manualmente tu navegador y ve a: `http://localhost:8501`

---

## 📋 CHECKLIST DE VERIFICACIÓN

Antes de la presentación, verifica:

- [ ] Entorno virtual creado y activado
- [ ] Todas las dependencias instaladas (`pip list` debería mostrar langchain, langgraph, etc.)
- [ ] Archivo `.env` configurado con GROQ_API_KEY real
- [ ] Carpeta `corpus/` con los 3 archivos .txt
- [ ] `python test_setup.py` pasa todos los tests
- [ ] `streamlit run app.py` ejecuta sin errores
- [ ] La interfaz web se abre correctamente
- [ ] El sistema responde al mensaje inicial

---

## 🆘 SOPORTE ADICIONAL

Si los problemas persisten:

1. **Revisa los logs:** Streamlit muestra errores detallados en la terminal
2. **Verifica versiones:** 
   ```bash
   python --version  # Debería ser 3.8+
   pip list | grep -E "langchain|streamlit"
   ```
3. **Reinstalación limpia:**
   ```bash
   # Eliminar entorno virtual
   rm -rf venv  # macOS/Linux
   rmdir /s venv  # Windows
   
   # Repetir desde el Paso 1
   ```

---

## ✅ ¡TODO LISTO!

Una vez completados todos los pasos y verificaciones, estarás listo para ejecutar y demostrar MEDI-IA-LEGAL.

**Comando para ejecutar:**
```bash
streamlit run app.py
```

**¡Disfruta la demo!** 🎉
