# ✅ CHECKLIST PRE-PRESENTACIÓN
# MEDI-IA-LEGAL - Verificación Final

## 🎯 15 MINUTOS ANTES DE LA PRESENTACIÓN

### ⚙️ CONFIGURACIÓN TÉCNICA

- [ ] **Entorno Virtual Activado**
  ```powershell
  # Verificar que aparece (venv) al inicio de la línea de comando
  # Si no: .\venv\Scripts\activate
  ```

- [ ] **Dependencias Instaladas**
  ```bash
  python test_setup.py
  # Debe mostrar todos ✓ OK
  ```

- [ ] **API Key Configurada**
  ```bash
  # Abrir .env y verificar que NO dice "tu_api_key_de_groq"
  # Debe tener: GROQ_API_KEY="gsk_..."
  ```

- [ ] **Corpus Legal Presente**
  ```bash
  ls corpus/
  # Debe mostrar: ley_2442.txt, codigo_civil.txt, interes_menor.txt
  ```

---

### 🖥️ APLICACIÓN FUNCIONANDO

- [ ] **Streamlit Ejecutándose**
  ```bash
  streamlit run app.py
  # Debe abrir navegador en http://localhost:8501
  ```

- [ ] **Mensaje de Bienvenida Funciona**
  ```
  Debe aparecer el saludo automático del sistema
  estableciendo los 3 puntos nodales
  ```

- [ ] **Prueba Rápida de Calculator**
  ```
  Escribe: "Activos 500M, deudas 100M"
  Verifica que invoca la herramienta y muestra cálculo
  ```

- [ ] **Prueba Rápida de RAG**
  ```
  Escribe: "¿Qué dice la ley sobre divorcio unilateral?"
  Verifica que consulta el corpus y cita Ley 2442
  ```

- [ ] **Prueba de Barrera Ética**
  ```
  Escribe: "Quiero el 80% de los bienes"
  Verifica que rechaza e invoca legal_analyst_tool
  ```

---

### 📂 ARCHIVOS ABIERTOS EN VS CODE

**Pestaña 1: app.py**
- Para mostrar la interfaz Streamlit
- Resaltar: st.session_state, invocación del grafo

**Pestaña 2: graph.py**
- Para mostrar el SUPERVISOR_SYSTEM_PROMPT
- Resaltar: StateGraph, router, workflow

**Pestaña 3: tools.py**
- Para mostrar las herramientas especializadas
- Resaltar: @tool decorator, setup_legal_rag_tool

**Pestaña 4: corpus/codigo_civil.txt**
- Para mostrar el corpus legal simulado
- Demostrar de dónde viene la información del RAG

**Pestaña 5: README.md**
- Para referencia rápida durante preguntas

---

### 🌐 NAVEGADOR

- [ ] **Pestaña 1: Streamlit App**
  ```
  http://localhost:8501
  Ventana principal de la demo
  ```

- [ ] **Pestaña 2: Groq Console (opcional)**
  ```
  https://console.groq.com/
  Por si preguntan sobre la API
  ```

- [ ] **Pestaña 3: LangGraph Docs (opcional)**
  ```
  https://langchain-ai.github.io/langgraph/
  Para referencias técnicas
  ```

---

### 💻 TERMINAL

- [ ] **Terminal 1: Streamlit Running**
  ```
  Debe mostrar:
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  ```

- [ ] **Terminal 2: Standby (opcional)**
  ```
  Con venv activado
  Por si necesitas ejecutar comandos rápidos
  ```

---

## 📝 DOCUMENTACIÓN LISTA

- [ ] **DEMO_GUIDE.md** - Abierto para referencia del script
- [ ] **EXAMPLES.md** - Abierto para copiar/pegar interacciones
- [ ] **README.md** - Para mostrar arquitectura del proyecto

---

## 🎤 PRESENTACIÓN PERSONAL

- [ ] **Slides/Presentación** (si aplica)
  - Arquitectura de Supervisor
  - Diagrama de flujo
  - Puntos nodales
  
- [ ] **Notas Preparadas**
  - Introducción (30 seg)
  - Explicación técnica (2 min)
  - Demo en vivo (10 min)
  - Cierre (1 min)

---

## 🧪 PLAN B (Por si algo falla)

### Si falla la conexión a internet:
- [ ] Tener screenshots de ejecuciones exitosas previas
- [ ] Tener grabación de video de la demo como backup

### Si falla Groq API:
- [ ] Tener configurado OpenAI como alternativa en .env
  ```env
  # Descomentar:
  OPENAI_API_KEY="tu_key"
  ```
- [ ] Modificar graph.py para usar ChatOpenAI
  ```python
  # from langchain_groq import ChatGroq
  from langchain_openai import ChatOpenAI
  # llm = ChatGroq(...)
  llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
  ```

### Si falla Streamlit:
- [ ] Ejecutar en Jupyter Notebook como alternativa
- [ ] O demostrar solo la lógica del grafo con prints

---

## 🎯 PUNTOS CLAVE A DESTACAR

Durante la presentación, ASEGÚRATE de mencionar:

1. **Arquitectura de Supervisor** ✨
   - "El Supervisor orquesta agentes especializados"
   
2. **RAG Legal** 📚
   - "Respuestas fundamentadas en corpus jurídico"
   
3. **Barrera Ética** ⚖️
   - "El sistema rechaza propuestas injustas"
   
4. **StateGraph** 🔄
   - "Mantiene contexto a través de la conversación"
   
5. **Prototipo en 1 hora** ⏱️
   - "Demostración de eficiencia del stack"

---

## 🚀 SECUENCIA DE DEMO (5 MINUTOS)

**Minuto 0-1: Introducción**
- Mostrar interfaz
- Explicar objetivo del sistema
- Mencionar Ley 2442 de 2024

**Minuto 1-2: Arquitectura**
- Abrir graph.py → Mostrar SUPERVISOR_SYSTEM_PROMPT
- Abrir tools.py → Mostrar herramientas
- Explicar flujo: Supervisor → Tools → Supervisor

**Minuto 2-4: Demo en Vivo**
- Input: "Activos 500M, deudas 100M"
- Mostrar invocación de calculate_society_split
- Input: "Quiero 80%"
- Mostrar barrera ética + RAG

**Minuto 4-5: Cierre**
- Resumen de componentes
- Aplicaciones potenciales
- Q&A

---

## 📊 MÉTRICAS PARA MENCIONAR

- ⚡ **LLM**: Llama3-8B (vía Groq) - Velocidad óptima
- 🧠 **Agentes**: 1 Supervisor + 2 Herramientas especializadas
- 📚 **Corpus**: 3 documentos legales simulados
- 🔧 **Tecnologías**: 8 (LangChain, LangGraph, Groq, Streamlit, ChromaDB, etc.)
- ⏱️ **Desarrollo**: Prototipo funcional en 1 hora
- 🎯 **Cobertura**: 3/3 puntos nodales de mediación

---

## ⚠️ ERRORES COMUNES A EVITAR

❌ **NO digas:** "Voy a ejecutar la aplicación..."
✅ **DI:** "Ya tengo la aplicación ejecutándose..."

❌ **NO digas:** "Espero que funcione..."
✅ **DI:** "Como pueden ver, el sistema..."

❌ **NO esperes** a que cargue algo en vivo
✅ **Ten todo pre-cargado** antes de empezar

❌ **NO improvises** las interacciones
✅ **Usa los ejemplos preparados** en EXAMPLES.md

---

## 🎉 VERIFICACIÓN FINAL

### TODO ESTÁ LISTO SI:

✅ Streamlit corre sin errores
✅ Mensaje de bienvenida aparece automáticamente
✅ Calculator funciona con input de prueba
✅ RAG responde preguntas sobre leyes
✅ Barrera ética rechaza propuestas injustas
✅ Tienes ejemplos preparados para copiar/pegar
✅ Conoces qué archivos mostrar y cuándo
✅ Tienes Plan B por si algo falla

---

## 📞 ÚLTIMA VERIFICACIÓN (30 SEGUNDOS ANTES)

1. **Respira** 😌
2. **Verifica que Streamlit está corriendo** 🟢
3. **Haz clic en "Reiniciar Conversación"** (sidebar) para empezar limpio 🔄
4. **Sonríe** 😊
5. **¡EMPIEZA!** 🚀

---

**¡MUCHA SUERTE! 🍀**

*Recuerda: Es un prototipo funcional. Si algo falla, explica el concepto y muestra el código. La arquitectura es lo importante.*
