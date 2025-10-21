# 📚 ÍNDICE DE DOCUMENTACIÓN
# MEDI-IA-LEGAL - Guía Completa

## 🎯 INICIO RÁPIDO

¿Primera vez con el proyecto? **Sigue este orden:**

1. 📄 **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Lee esto PRIMERO
   - Resumen ejecutivo del proyecto
   - Qué se ha construido
   - Métricas y características

2. 📥 **[INSTALL.md](INSTALL.md)** - Instalación paso a paso
   - Configuración del entorno
   - Instalación de dependencias
   - Solución de problemas comunes

3. ✅ **[CHECKLIST.md](CHECKLIST.md)** - Verificación pre-presentación
   - Lista de verificación completa
   - Preparación de archivos
   - Últimos pasos antes de presentar

4. 🎬 **[DEMO_GUIDE.md](DEMO_GUIDE.md)** - Script de presentación
   - Guión completo para la demo
   - Timing y secuencia
   - Puntos clave a destacar

---

## 📖 DOCUMENTACIÓN POR CATEGORÍA

### 🚀 Configuración e Instalación

| Documento | Descripción | Cuándo usarlo |
|-----------|-------------|---------------|
| **[INSTALL.md](INSTALL.md)** | Guía completa de instalación | Primera instalación o problemas de setup |
| **[COMMANDS.md](COMMANDS.md)** | Referencia de comandos útiles | Necesitas un comando específico |
| **test_setup.py** | Script de verificación | Validar que todo está instalado |

### 📋 Documentación del Proyecto

| Documento | Descripción | Cuándo usarlo |
|-----------|-------------|---------------|
| **[README.md](README.md)** | Documentación principal | Overview general del proyecto |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Resumen ejecutivo | Entender qué se construyó |
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | Diagramas de arquitectura | Entender la estructura técnica |

### 🎭 Presentación y Demo

| Documento | Descripción | Cuándo usarlo |
|-----------|-------------|---------------|
| **[DEMO_GUIDE.md](DEMO_GUIDE.md)** | Script de presentación | Preparar/ejecutar la demo |
| **[EXAMPLES.md](EXAMPLES.md)** | Casos de uso y ejemplos | Buscar interacciones de ejemplo |
| **[CHECKLIST.md](CHECKLIST.md)** | Verificación pre-demo | Antes de la presentación |

### 🔧 Referencia Técnica

| Documento | Descripción | Cuándo usarlo |
|-----------|-------------|---------------|
| **[COMMANDS.md](COMMANDS.md)** | Comandos de desarrollo | Referencia rápida de comandos |
| **tools.py** | Código de herramientas | Entender los agentes especializados |
| **graph.py** | Código del grafo | Entender la orquestación |
| **app.py** | Código de la UI | Entender la interfaz Streamlit |

---

## 🗺️ FLUJO DE TRABAJO RECOMENDADO

### Para Instalación Inicial

```
1. Leer PROJECT_SUMMARY.md (5 min)
   ↓
2. Seguir INSTALL.md (10 min)
   ↓
3. Ejecutar test_setup.py (1 min)
   ↓
4. Probar app: streamlit run app.py
```

### Para Preparar Presentación

```
1. Revisar CHECKLIST.md (5 min)
   ↓
2. Estudiar DEMO_GUIDE.md (10 min)
   ↓
3. Leer EXAMPLES.md (5 min)
   ↓
4. Practicar demo (10 min)
```

### Para Entender el Código

```
1. Leer ARCHITECTURE.md (5 min)
   ↓
2. Revisar tools.py (línea por línea)
   ↓
3. Revisar graph.py (línea por línea)
   ↓
4. Revisar app.py (línea por línea)
```

---

## 📂 ESTRUCTURA DE ARCHIVOS

### Archivos de Código (Python)

```
📄 app.py                # Frontend Streamlit
📄 graph.py              # Grafo LangGraph (core)
📄 tools.py              # Herramientas/Agentes
📄 test_setup.py         # Script de verificación
```

### Documentación (Markdown)

```
📖 README.md             # Documentación principal
📖 PROJECT_SUMMARY.md    # Resumen ejecutivo
📖 INSTALL.md            # Guía de instalación
📖 DEMO_GUIDE.md         # Script de presentación
📖 EXAMPLES.md           # Ejemplos de uso
📖 CHECKLIST.md          # Verificación pre-demo
📖 ARCHITECTURE.md       # Diagramas técnicos
📖 COMMANDS.md           # Referencia de comandos
📖 INDEX.md              # Este archivo
```

### Scripts de Automatización (PowerShell)

```
⚙️ setup.ps1             # Instalación automática
⚙️ run.ps1               # Ejecución rápida
```

### Configuración

```
🔧 requirements.txt      # Dependencias Python
🔧 .env                  # Variables de entorno
🔧 .gitignore            # Exclusiones Git
🔧 .streamlit/config.toml # Config Streamlit
```

### Datos

```
📚 corpus/
   ├── ley_2442.txt      # Ley divorcio unilateral
   ├── codigo_civil.txt  # Sociedad conyugal
   └── interes_menor.txt # Interés del menor
```

---

## 🎯 CASOS DE USO DE LA DOCUMENTACIÓN

### "Es mi primera vez, ¿por dónde empiezo?"
1. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Entender qué es el proyecto
2. **[INSTALL.md](INSTALL.md)** - Instalarlo
3. **[README.md](README.md)** - Profundizar

### "Necesito instalar el proyecto"
1. **[INSTALL.md](INSTALL.md)** - Sigue las instrucciones
2. **test_setup.py** - Verifica la instalación
3. **[COMMANDS.md](COMMANDS.md)** - Si necesitas comandos específicos

### "Voy a presentar el proyecto"
1. **[CHECKLIST.md](CHECKLIST.md)** - Verificación completa
2. **[DEMO_GUIDE.md](DEMO_GUIDE.md)** - Script de presentación
3. **[EXAMPLES.md](EXAMPLES.md)** - Ejemplos para copiar/pegar

### "Quiero entender la arquitectura"
1. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Diagramas visuales
2. **graph.py** - Código del grafo
3. **tools.py** - Código de herramientas

### "Necesito resolver un problema técnico"
1. **[INSTALL.md](INSTALL.md)** - Sección de troubleshooting
2. **[COMMANDS.md](COMMANDS.md)** - Comandos de debugging
3. **test_setup.py** - Diagnóstico automático

### "Quiero extender el proyecto"
1. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Entender la estructura
2. **tools.py** - Ver cómo añadir herramientas
3. **graph.py** - Ver cómo modificar el grafo

---

## 📊 CONTENIDO POR DOCUMENTO

### 📄 PROJECT_SUMMARY.md
- ✅ Resumen ejecutivo
- ✅ Estructura completa del proyecto
- ✅ Componentes implementados
- ✅ Pasos para ejecutar
- ✅ Métricas del proyecto
- ✅ Tecnologías utilizadas

### 📥 INSTALL.md
- ✅ Instalación automática (Windows)
- ✅ Instalación manual (multiplataforma)
- ✅ Configuración de API keys
- ✅ Troubleshooting detallado
- ✅ Checklist de verificación

### 📖 README.md
- ✅ Descripción del proyecto
- ✅ Arquitectura
- ✅ Instalación básica
- ✅ Ejecución
- ✅ Flujo de prueba
- ✅ Tecnologías

### 🎬 DEMO_GUIDE.md
- ✅ Checklist pre-presentación
- ✅ Script de demostración
- ✅ Timing por sección
- ✅ Manejo de errores en vivo
- ✅ Preguntas frecuentes
- ✅ Puntos clave a destacar

### 💬 EXAMPLES.md
- ✅ Caso 1: Flujo completo exitoso
- ✅ Caso 2: Barrera ética (división injusta)
- ✅ Caso 3: Barrera ética (alimentos)
- ✅ Caso 4: Consulta legal específica
- ✅ Caso 5: Cálculo financiero complejo
- ✅ Caso 6: Desacuerdo y re-negociación
- ✅ Interacciones rápidas para demo

### ✅ CHECKLIST.md
- ✅ Verificación técnica (15 min antes)
- ✅ Aplicación funcionando
- ✅ Archivos abiertos en VS Code
- ✅ Navegador preparado
- ✅ Plan B por si algo falla
- ✅ Puntos clave a destacar
- ✅ Secuencia de demo

### 🏗️ ARCHITECTURE.md
- ✅ Diagrama de flujo principal (Mermaid)
- ✅ Arquitectura de componentes
- ✅ Flujo de decisión del supervisor
- ✅ Ciclo de mediación (3 puntos)
- ✅ Stack tecnológico
- ✅ Flujo de datos (sequence diagram)
- ✅ Extensiones futuras

### ⚡ COMMANDS.md
- ✅ Inicio rápido
- ✅ Gestión del entorno virtual
- ✅ Gestión de dependencias
- ✅ Testing y verificación
- ✅ Ejecución
- ✅ Debugging
- ✅ Limpieza
- ✅ Comandos de emergencia

---

## 🔍 BÚSQUEDA RÁPIDA

### Necesito información sobre...

**Instalación:**
- Paso a paso → [INSTALL.md](INSTALL.md)
- Comandos → [COMMANDS.md](COMMANDS.md)
- Verificación → test_setup.py

**Presentación:**
- Script completo → [DEMO_GUIDE.md](DEMO_GUIDE.md)
- Ejemplos → [EXAMPLES.md](EXAMPLES.md)
- Checklist → [CHECKLIST.md](CHECKLIST.md)

**Arquitectura:**
- Diagramas → [ARCHITECTURE.md](ARCHITECTURE.md)
- Código Grafo → graph.py
- Código Herramientas → tools.py

**Troubleshooting:**
- Problemas comunes → [INSTALL.md](INSTALL.md) (sección Troubleshooting)
- Comandos útiles → [COMMANDS.md](COMMANDS.md)
- Test automático → test_setup.py

**API Keys:**
- Configuración → [INSTALL.md](INSTALL.md) (Paso 5)
- Dónde obtenerla → [README.md](README.md)
- Verificación → test_setup.py

---

## 🎓 NIVELES DE LECTURA

### Nivel 1: Principiante (30 min)
```
1. PROJECT_SUMMARY.md     (10 min)
2. README.md              (10 min)
3. INSTALL.md             (10 min)
```

### Nivel 2: Presentador (1 hora)
```
1. PROJECT_SUMMARY.md     (10 min)
2. DEMO_GUIDE.md          (20 min)
3. EXAMPLES.md            (15 min)
4. CHECKLIST.md           (15 min)
```

### Nivel 3: Desarrollador (2 horas)
```
1. PROJECT_SUMMARY.md     (10 min)
2. ARCHITECTURE.md        (20 min)
3. tools.py               (30 min)
4. graph.py               (30 min)
5. app.py                 (30 min)
```

### Nivel 4: Experto (Todo)
```
Lee todos los documentos +
Estudia todo el código +
Practica extensiones
```

---

## 📞 AYUDA Y SOPORTE

### Problemas de Instalación
→ **[INSTALL.md](INSTALL.md)** sección "Solución de Problemas"

### Errores al Ejecutar
→ **test_setup.py** para diagnóstico
→ **[COMMANDS.md](COMMANDS.md)** sección "Debugging"

### Dudas sobre Arquitectura
→ **[ARCHITECTURE.md](ARCHITECTURE.md)**
→ Código fuente (tools.py, graph.py)

### Preparación de Demo
→ **[DEMO_GUIDE.md](DEMO_GUIDE.md)**
→ **[CHECKLIST.md](CHECKLIST.md)**

---

## 🗂️ ORGANIZACIÓN DE ARCHIVOS

### Por Propósito

**Código Ejecutable:**
- app.py, graph.py, tools.py, test_setup.py

**Documentación:**
- Todos los .md

**Configuración:**
- requirements.txt, .env, .gitignore, .streamlit/

**Scripts:**
- setup.ps1, run.ps1

**Datos:**
- corpus/

### Por Frecuencia de Uso

**Uso Diario:**
- app.py, COMMANDS.md, DEMO_GUIDE.md

**Uso Ocasional:**
- README.md, INSTALL.md, test_setup.py

**Referencia:**
- ARCHITECTURE.md, EXAMPLES.md, PROJECT_SUMMARY.md

---

## 🎯 OBJETIVOS DE CADA DOCUMENTO

| Documento | Objetivo Principal |
|-----------|-------------------|
| PROJECT_SUMMARY | Entender QUÉ se construyó |
| INSTALL | Aprender CÓMO instalarlo |
| README | Overview GENERAL |
| DEMO_GUIDE | CÓMO presentarlo |
| EXAMPLES | QUÉ decir/escribir |
| CHECKLIST | QUÉ verificar |
| ARCHITECTURE | CÓMO funciona técnicamente |
| COMMANDS | QUÉ comandos usar |
| INDEX | DÓNDE encontrar información |

---

## ✨ CONTRIBUCIONES FUTURAS

Si quieres extender la documentación:

1. **FAQ.md** - Preguntas frecuentes
2. **TUTORIAL.md** - Tutorial paso a paso
3. **API.md** - Documentación de API
4. **TESTING.md** - Guía de tests
5. **DEPLOYMENT.md** - Despliegue en producción

---

## 📌 MARCADORES ÚTILES

Marca estas páginas en tu navegador/editor:

1. **[CHECKLIST.md](CHECKLIST.md)** - Para antes de presentar
2. **[EXAMPLES.md](EXAMPLES.md)** - Para copiar/pegar
3. **[COMMANDS.md](COMMANDS.md)** - Para comandos rápidos
4. **[DEMO_GUIDE.md](DEMO_GUIDE.md)** - Para el script

---

## 🎉 RESUMEN

Este índice te ayuda a navegar toda la documentación de MEDI-IA-LEGAL.

**Para empezar:** [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
**Para instalar:** [INSTALL.md](INSTALL.md)
**Para presentar:** [DEMO_GUIDE.md](DEMO_GUIDE.md)

**¡Todo está documentado! Encuentra lo que necesitas y adelante! 🚀**

---

*Índice general de MEDI-IA-LEGAL - Sistema de Mediación Inteligente*
