# 🚀 EMPEZAR AHORA - GUÍA DE 5 MINUTOS

## ⚡ INICIO ULTRA RÁPIDO

### Paso 1: Obtén tu API Key de Groq (2 minutos)

1. Ve a: **https://console.groq.com/**
2. Crea una cuenta gratuita (o inicia sesión)
3. En el menú lateral, haz clic en **"API Keys"**
4. Haz clic en **"Create API Key"**
5. Dale un nombre (ej: "medi-ia-legal")
6. Copia la key generada (formato: `gsk_...`)

### Paso 2: Configura el Proyecto (1 minuto)

1. Abre el archivo **`.env`** en tu editor
2. Busca esta línea:
   ```
   GROQ_API_KEY="tu_api_key_de_groq"
   ```
3. Reemplaza `tu_api_key_de_groq` con tu key real:
   ```
   GROQ_API_KEY="gsk_tu_key_copiada_aqui"
   ```
4. Guarda el archivo

### Paso 3: Instala y Ejecuta (2 minutos)

Abre PowerShell en VS Code y ejecuta:

```powershell
# Opción A: Automático (Recomendado)
.\setup.ps1

# Opción B: Manual
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Luego ejecuta:

```powershell
streamlit run app.py
```

**¡LISTO!** La aplicación se abrirá en tu navegador.

---

## ✅ VERIFICACIÓN RÁPIDA

Si todo está bien, deberías ver:

1. ✅ Navegador abre en `http://localhost:8501`
2. ✅ Título: "⚖️ MEDI-IA-LEGAL: Mediación de Divorcio Asistida por IA"
3. ✅ Mensaje de bienvenida automático del sistema
4. ✅ Sidebar con información del sistema

---

## 🧪 PRUEBA RÁPIDA (30 segundos)

En el chat, escribe:

```
Tenemos activos por 500 millones y deudas por 100 millones
```

**Deberías ver:**
- El sistema invoca `calculate_society_split`
- Muestra el cálculo: 200 millones para cada cónyuge

**Si funciona: ¡ÉXITO! 🎉 Estás listo para la demo.**

---

## 🚨 ¿PROBLEMAS?

### Error: "Import could not be resolved"
```powershell
# Asegúrate de activar el entorno virtual
.\venv\Scripts\activate
# Reinstala
pip install -r requirements.txt
```

### Error: "GROQ_API_KEY not found"
- Verifica que el archivo `.env` tenga tu key real
- NO uses comillas simples, solo dobles
- Reinicia la aplicación después de editar `.env`

### Error: Streamlit no abre
- Abre manualmente: `http://localhost:8501`
- O usa otro puerto: `streamlit run app.py --server.port 8502`

---

## 📚 PRÓXIMOS PASOS

### Para la Presentación:
1. Lee **[DEMO_GUIDE.md](DEMO_GUIDE.md)** (10 min)
2. Revisa **[EXAMPLES.md](EXAMPLES.md)** (5 min)
3. Verifica **[CHECKLIST.md](CHECKLIST.md)** (5 min)

### Para Entender el Código:
1. Lee **[ARCHITECTURE.md](ARCHITECTURE.md)**
2. Abre `tools.py` y estúdialo línea por línea
3. Abre `graph.py` y estúdialo línea por línea
4. Abre `app.py` y estúdialo línea por línea

### Para Extender el Proyecto:
1. Añade nuevas herramientas en `tools.py`
2. Modifica el prompt del supervisor en `graph.py`
3. Añade más documentos al corpus legal

---

## 🎯 ATAJOS DE TECLADO ÚTILES

En Streamlit (navegador):
- **R**: Rerun app
- **C**: Clear cache

En Terminal:
- **Ctrl + C**: Detener Streamlit

---

## 📞 AYUDA RÁPIDA

### "¿Qué archivo abro para...?"

- **Ver el supervisor**: `graph.py`
- **Ver las herramientas**: `tools.py`
- **Ver la interfaz**: `app.py`
- **Ver el corpus legal**: `corpus/`
- **Ver ejemplos de uso**: `EXAMPLES.md`
- **Ver comandos**: `COMMANDS.md`

### "¿Cómo hago...?"

- **Reiniciar la conversación**: Botón en sidebar
- **Ver logs**: Terminal donde ejecutaste `streamlit run app.py`
- **Cambiar puerto**: `streamlit run app.py --server.port 8502`
- **Detener app**: `Ctrl + C` en la terminal

---

## 🎬 EJEMPLO DE DEMO RÁPIDA (2 MIN)

### Mensaje 1:
```
Hola, queremos iniciar un divorcio.
```

### Mensaje 2:
```
Tenemos activos por 500 millones y deudas por 100 millones.
```
👉 Muestra invocación de `Financial_Calculator_Agent`

### Mensaje 3:
```
Quiero el 80% de los bienes.
```
👉 Muestra **Barrera Ética** + invocación de `Legal_Analyst_Agent`

### Mensaje 4:
```
Acepto la división 50/50.
```
👉 Muestra confirmación y avance al siguiente punto

**¡Con estos 4 mensajes demuestras TODO el sistema! ⚡**

---

## 💡 TIPS PRO

1. **Antes de la demo**: Ejecuta una vez completa para calentar el sistema
2. **Ten EXAMPLES.md abierto**: Para copiar/pegar interacciones
3. **Usa el botón "Reiniciar"**: Para empezar limpio en la demo
4. **Practica el flujo**: Al menos 1 vez antes de presentar

---

## ✨ CHECKLIST FINAL (1 MIN)

Antes de presentar, verifica:

- [ ] Streamlit corriendo sin errores
- [ ] API key configurada en `.env`
- [ ] Mensaje de bienvenida aparece
- [ ] Probaste un cálculo financiero
- [ ] Probaste la barrera ética
- [ ] Tienes EXAMPLES.md y DEMO_GUIDE.md abiertos

**Si todos ✅: ¡ADELANTE! 🚀**

---

## 🎉 ¡ESTÁS LISTO!

Has creado un sistema completo de mediación inteligente con:

- ✅ Arquitectura de Supervisor (LangGraph)
- ✅ 2 Agentes especializados (Calculator + RAG)
- ✅ Barrera Ética de Contención
- ✅ Interfaz Streamlit moderna
- ✅ Documentación completa

**Tiempo total de setup: 5 minutos**
**Tiempo total de demo: 5 minutos**
**Impacto: MÁXIMO 💯**

---

## 📖 MÁS INFORMACIÓN

- **Índice completo**: [INDEX.md](INDEX.md)
- **Resumen del proyecto**: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **Guía de instalación**: [INSTALL.md](INSTALL.md)
- **Script de demo**: [DEMO_GUIDE.md](DEMO_GUIDE.md)

---

**¡MUCHA SUERTE CON TU PRESENTACIÓN! 🍀✨**

*Si tienes algún problema, revisa INSTALL.md sección "Troubleshooting"*
