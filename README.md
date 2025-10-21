# MEDI-IA-LEGAL 🏛️⚖️ Sistema de Mediación Inteligente para Propuestas de Divorcio basado en LangGraph y la Ley 2442 de 2024.

## 📋 Descripción
MEDI-IA-LEGAL es un prototipo funcional que implementa un sistema de mediación asistida por IA para facilitar la creación de propuestas de divorcio justas y legales bajo la legislación colombiana. Utiliza la arquitectura de Supervisor de LangGraph para orquestar agentes especializados.

## 🏗️ Arquitectura
- **Mediator_Supervisor_Agent**: Orquestador central que guía la conversación.
- **Legal_Analyst_Agent**: Herramienta RAG sobre corpus legal simulado.
- **Financial_Calculator_Agent**: Herramienta para cálculos financieros deterministas.
- **StateGraph**: Gestión del estado de la conversación.

## 🚀 Instalación y Configuración

### Paso 1: Crear y Activar Entorno Virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:

Bash

python -m venv venv
source venv/bin/activate
Paso 2: Instalar Dependencias
Bash

pip install -r requirements.txt
Paso 3: Configurar API Keys
Edita el archivo .env y añade tu API key de Groq:

Fragmento de código

GROQ_API_KEY="tu_api_key_real_aqui"
¿Dónde obtener la API key de Groq?

Visita: https://console.groq.com/

Crea una cuenta gratuita.

Ve a "API Keys" y genera una nueva key.

📂 Estructura del Proyecto
MEDI-IA-LEGAL/
│
├── corpus/               # Corpus legal simulado
│   ├── ley_2442.txt      # Ley de divorcio unilateral
│   ├── codigo_civil.txt  # Normas sobre sociedad conyugal
│   └── interes_menor.txt # Principio del interés superior del menor
│
├── tools.py              # Agentes especializados (herramientas)
├── graph.py              # Grafo de mediación (LangGraph)
├── app.py                # Interfaz Streamlit
├── requirements.txt      # Dependencias
├── .env                  # Variables de entorno (API keys)
└── README.md             # Este archivo
▶️ Ejecución
Con el entorno virtual activado, ejecuta:

Bash

streamlit run app.py
La aplicación se abrirá en tu navegador en http://localhost:8501

🧪 Flujo de Prueba
Prueba 1: Flujo Normal
Inicio: El sistema te dará la bienvenida y establecerá la agenda.

Propuesta de bienes:

"Quiero empezar con los bienes. Tenemos activos por 500 millones y deudas por 100 millones."
Cálculo: El supervisor invocará al Financial_Calculator_Agent.

Resultado: Verás un cálculo de división 50/50.

Prueba 2: Barrera Ética
Propuesta injusta:

"Quiero el 80% de los bienes."
Intervención: El supervisor rechazará la propuesta.

Citación legal: Invocará al Legal_Analyst_Agent para citar la ley del 50/50.

Redirección: Pedirá reconsiderar la propuesta.

🛠️ Tecnologías Utilizadas
LangChain: Framework para aplicaciones con LLMs

LangGraph: Orquestación de agentes con grafos de estado

Groq: LLM rápido (Llama3) para la demo

Streamlit: Interfaz de usuario web

ChromaDB: Vector store para RAG

HuggingFace Embeddings: Embeddings para búsqueda semántica

📚 Puntos Nodales de Mediación
💰 Liquidación de la Sociedad Conyugal: División de bienes y deudas.

💵 Obligaciones Alimentarias: Acuerdos sobre pensiones.

👨‍👩‍👧‍👦 Acuerdos sobre Hijos Menores: Custodia, visitas y alimentos.

⚖️ Barrera Ética de Contención
El sistema implementa una barrera ética que:

Detecta propuestas injustas o ilegales.

Interviene activamente para corregir.

Cita la legislación relevante.

Solicita reconsideración de propuestas.

🔧 Troubleshooting
Error: Import "dotenv" could not be resolved
Solución: Asegúrate de haber instalado las dependencias:

Bash

pip install -r requirements.txt
Error: GROQ_API_KEY not found
Solución: Verifica que el archivo .env existe y contiene tu API key válida.

Error al cargar el corpus
Solución: Verifica que la carpeta corpus/ existe y contiene los 3 archivos .txt.

📄 Licencia
Prototipo educacional para demostración de arquitecturas de IA multi-agente.

👨‍💻 Desarrollo
Desarrollado como prototipo funcional en 1 hora para presentación.

⚠️ Disclaimer: Este es un prototipo educacional. No constituye asesoría legal real. Para casos reales de divorcio, consulta con un abogado certificado.
