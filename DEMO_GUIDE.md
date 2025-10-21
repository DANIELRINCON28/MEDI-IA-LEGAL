# 🎯 GUÍA RÁPIDA DE PRESENTACIÓN
# MEDI-IA-LEGAL - Demo en 1 Hora

## ⏱️ CHECKLIST PRE-PRESENTACIÓN (5 minutos)

### ✅ Configuración Inicial
- [ ] Abrir terminal en VS Code
- [ ] Activar entorno virtual: `.\venv\Scripts\activate`
- [ ] Verificar que `.env` tiene tu GROQ_API_KEY real
- [ ] Ejecutar: `streamlit run app.py`
- [ ] Verificar que la app se abre en el navegador

---

## 🎬 SCRIPT DE DEMOSTRACIÓN (15 minutos)

### 📍 Punto 1: Introducción al Sistema (2 minutos)

**Hablar mientras se muestra la interfaz:**

> "MEDI-IA-LEGAL es un sistema de mediación inteligente que implementa la arquitectura de Supervisor de LangGraph. El objetivo es facilitar la creación de propuestas de divorcio justas bajo la Ley 2442 de 2024 en Colombia."

**Mostrar:**
- Interfaz de Streamlit
- Sidebar con información del sistema
- Mencionar las 3 herramientas: Supervisor, Legal Analyst (RAG), Financial Calculator

---

### 📍 Punto 2: Arquitectura del Sistema (3 minutos)

**Explicar mientras se muestra el código:**

> "La arquitectura se basa en tres componentes clave:"

1. **Abrir `tools.py`** - Mostrar:
   ```python
   @tool
   def calculate_society_split(...)
   ```
   - Herramienta de cálculo financiero determinista
   
   ```python
   def setup_legal_rag_tool()
   ```
   - Herramienta RAG sobre corpus legal (ChromaDB + HuggingFace Embeddings)

2. **Abrir `graph.py`** - Mostrar:
   ```python
   SUPERVISOR_SYSTEM_PROMPT
   ```
   - Prompt del mediador con instrucciones de los 3 puntos nodales
   - Barrera ética de contención
   
   ```python
   workflow = StateGraph(GraphState)
   ```
   - StateGraph para gestionar la conversación
   - Nodos: supervisor + tools
   - Router condicional

3. **Abrir `app.py`** - Mostrar:
   - Integración con Streamlit
   - Manejo del estado de sesión

---

### 📍 Punto 3: Demo en Vivo - Flujo Normal (5 minutos)

**Volver a la aplicación de Streamlit**

**Interacción 1: Saludo**
```
Usuario: "Hola, estoy listo para comenzar."
```

**Esperado:** El sistema da bienvenida y establece la agenda de los 3 puntos nodales.

---

**Interacción 2: Propuesta de Bienes (invocar herramienta financiera)**
```
Usuario: "Quiero empezar con los bienes. Tenemos activos por 500 millones y deudas por 100 millones."
```

**Esperado:** 
- El supervisor detecta que necesita hacer un cálculo
- Invoca `calculate_society_split`
- Muestra el cálculo de división 50/50
- Explica: "400 millones netos → 200 millones para cada cónyuge"

**Punto clave para destacar:**
> "Observen cómo el sistema invocó automáticamente la herramienta de cálculo financiero. Esto es el Supervisor orquestando los agentes especializados."

---

### 📍 Punto 4: Demo en Vivo - Barrera Ética (5 minutos)

**Interacción 3: Propuesta Injusta (activar barrera ética + RAG)**
```
Usuario: "Quiero el 80% de los bienes para mí."
```

**Esperado:**
- El supervisor detecta inequidad
- NO acepta la propuesta
- Señala la desviación de la norma legal
- Invoca `legal_analyst_tool` para consultar el corpus
- Cita: "Código Civil establece división 50/50"
- Pide reconsiderar

**Punto clave para destacar:**
> "Esta es la Barrera Ética de Contención en acción. El sistema no solo rechaza la propuesta injusta, sino que cita la legislación relevante usando RAG sobre el corpus legal."

**Mostrar en VS Code:** Abrir `corpus/codigo_civil.txt` para mostrar de dónde viene la información.

---

**Interacción 4: Propuesta Corregida**
```
Usuario: "Entendido, acepto la división 50/50."
```

**Esperado:** El supervisor acepta y avanza al siguiente punto (Alimentos).

---

### 📍 Punto 5: Cierre y Ventajas del Sistema (3 minutos)

**Resumir ventajas:**

1. **Arquitectura Modular:**
   - Supervisor orquesta agentes especializados
   - Fácil añadir nuevas herramientas
   
2. **RAG Legal:**
   - Respuestas fundamentadas en corpus legal
   - Verificación automática de legalidad
   
3. **Barrera Ética:**
   - Protección contra propuestas injustas
   - Intervención proactiva con fundamentación legal
   
4. **Estado Persistente:**
   - StateGraph mantiene contexto de la conversación
   - Seguimiento de acuerdos punto por punto

---

## 🚨 MANEJO DE ERRORES EN VIVO

### Error: API Key no configurada
**Solución:** 
```powershell
# Abrir .env y pegar la key real
GROQ_API_KEY="gsk_tu_key_real_aquí"
# Reiniciar la app
```

### Error: Módulos no instalados
**Solución:**
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Error: Corpus no encontrado
**Solución:**
```powershell
# Verificar que existe:
ls corpus/
# Debe mostrar: ley_2442.txt, codigo_civil.txt, interes_menor.txt
```

---

## 🎤 PREGUNTAS FRECUENTES ANTICIPADAS

### P: ¿Por qué usar LangGraph en vez de solo LangChain?
**R:** LangGraph permite orquestación compleja con grafos de estado. Ideal para conversaciones multi-paso con decisiones condicionales (router) y herramientas especializadas.

### P: ¿Cómo se escalaría a producción?
**R:** 
- Corpus legal completo (no simulado)
- Base de datos persistente para sesiones
- Autenticación de usuarios
- Logs y métricas
- Deployment en cloud (Azure/AWS)

### P: ¿Qué pasa si las partes no llegan a acuerdo?
**R:** El sistema puede generar un "acta de mediación" con puntos en desacuerdo para revisión judicial.

### P: ¿Se puede usar con otros LLMs?
**R:** Sí, es modular. Solo cambiar `ChatGroq` por `ChatOpenAI`, `ChatAnthropic`, etc.

---

## 📊 MÉTRICAS DE ÉXITO PARA DESTACAR

- ⏱️ **Tiempo de desarrollo:** 1 hora (prototipo funcional)
- 🧠 **Agentes:** 3 (Supervisor + 2 herramientas especializadas)
- 📚 **Base legal:** 3 documentos del corpus
- 🔧 **Tecnologías:** 8 (LangChain, LangGraph, Groq, Streamlit, ChromaDB, etc.)
- ✅ **Puntos nodales cubiertos:** 3/3

---

## 🎯 PUNTOS CLAVE PARA ENFATIZAR

1. **Arquitectura de Supervisor** = Escalabilidad
2. **RAG Legal** = Fundamentación jurídica automática
3. **Barrera Ética** = Responsabilidad de la IA
4. **StateGraph** = Manejo complejo de conversaciones
5. **Prototipo funcional en 1 hora** = Eficiencia del stack tecnológico

---

## 🏁 CIERRE DE LA PRESENTACIÓN

> "MEDI-IA-LEGAL demuestra cómo la arquitectura de agentes multi-herramienta de LangGraph puede resolver problemas complejos del mundo real. Este prototipo es extensible a otros dominios legales, médicos o financieros donde se requiera mediación experta, verificación normativa y decisiones éticas."

**Llamado a la acción:**
> "El código completo está disponible. Los invito a explorar el grafo, experimentar con nuevas herramientas y adaptar el sistema a sus propios casos de uso."

---

## 📝 NOTAS FINALES

- Tener el README.md abierto en otra pestaña para referencia
- Preparar 2-3 ejemplos adicionales de interacciones por si hay tiempo
- Tener abierto el terminal con el entorno virtual activado
- Bookmark a https://console.groq.com/ por si preguntan sobre la API
