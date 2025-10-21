# 🏗️ ARQUITECTURA DEL SISTEMA MEDI-IA-LEGAL

## Diagrama de Flujo Principal

```mermaid
graph TD
    A[👤 Usuario] -->|Mensaje| B[Streamlit App]
    B -->|Invoke| C[LangGraph StateGraph]
    C --> D{Supervisor Node}
    D -->|Analiza mensaje| E{¿Necesita herramientas?}
    E -->|Sí, tool_calls| F[Tool Node]
    E -->|No| G[Respuesta directa]
    F --> H{¿Qué herramienta?}
    H -->|Cálculo financiero| I[Financial Calculator]
    H -->|Consulta legal| J[Legal Analyst RAG]
    I -->|Resultado| D
    J -->|Documentos relevantes| D
    D -->|Genera respuesta| K[LLM - Llama3]
    K -->|Respuesta| B
    B -->|Muestra| A
    G -->|Respuesta| B
```

## Arquitectura de Componentes

```mermaid
graph LR
    subgraph "Frontend"
        A[Streamlit UI]
    end
    
    subgraph "LangGraph Supervisor"
        B[Mediator Supervisor Agent]
        C[StateGraph]
        D[Router Function]
    end
    
    subgraph "Herramientas/Agentes"
        E[Financial Calculator]
        F[Legal Analyst RAG]
    end
    
    subgraph "Backend"
        G[Groq API - Llama3]
        H[ChromaDB Vector Store]
        I[HuggingFace Embeddings]
    end
    
    subgraph "Datos"
        J[Corpus Legal]
        K[Session State]
    end
    
    A <--> B
    B <--> C
    B <--> D
    D --> E
    D --> F
    B <--> G
    F <--> H
    H <--> I
    I <--> J
    C <--> K
```

## Flujo de Decisión del Supervisor

```mermaid
flowchart TD
    Start([Usuario envía mensaje]) --> A[Supervisor recibe mensaje]
    A --> B{¿Es inequitativo?}
    B -->|Sí| C[Rechazar propuesta]
    C --> D[Invocar Legal Analyst]
    D --> E[Citar ley relevante]
    E --> F[Pedir reconsideración]
    
    B -->|No| G{¿Necesita cálculo?}
    G -->|Sí| H[Invocar Financial Calculator]
    H --> I[Mostrar resultado]
    
    G -->|No| J{¿Necesita consulta legal?}
    J -->|Sí| K[Invocar Legal Analyst RAG]
    K --> L[Devolver información legal]
    
    J -->|No| M[Respuesta directa]
    
    F --> End([Enviar respuesta al usuario])
    I --> End
    L --> End
    M --> End
```

## Ciclo de Mediación (3 Puntos Nodales)

```mermaid
stateDiagram-v2
    [*] --> Bienvenida
    Bienvenida --> Punto1_Bienes
    
    state Punto1_Bienes {
        [*] --> Solicitar_Datos_Bienes
        Solicitar_Datos_Bienes --> Calcular_Division
        Calcular_Division --> Verificar_Equidad
        Verificar_Equidad --> Acuerdo_Bienes: ✅ Justo
        Verificar_Equidad --> Rechazar_Propuesta: ❌ Injusto
        Rechazar_Propuesta --> Solicitar_Datos_Bienes
    }
    
    Punto1_Bienes --> Punto2_Alimentos: Acuerdo confirmado
    
    state Punto2_Alimentos {
        [*] --> Solicitar_Ingresos
        Solicitar_Ingresos --> Analizar_Obligaciones
        Analizar_Obligaciones --> Acuerdo_Alimentos
    }
    
    Punto2_Alimentos --> Punto3_Hijos: Acuerdo confirmado
    
    state Punto3_Hijos {
        [*] --> Solicitar_Info_Hijos
        Solicitar_Info_Hijos --> Verificar_Interes_Menor
        Verificar_Interes_Menor --> Acuerdo_Hijos
    }
    
    Punto3_Hijos --> Resumen_Final: Todos los puntos acordados
    Resumen_Final --> [*]
```

## Stack Tecnológico

```mermaid
graph TB
    subgraph "Capa de Presentación"
        A[Streamlit 🖥️]
    end
    
    subgraph "Capa de Orquestación"
        B[LangGraph 🕸️]
        C[LangChain 🔗]
    end
    
    subgraph "Capa de IA"
        D[Groq API ⚡]
        E[Llama3-8B 🧠]
    end
    
    subgraph "Capa de Conocimiento"
        F[ChromaDB 🗄️]
        G[HuggingFace Embeddings 🤗]
        H[Corpus Legal 📚]
    end
    
    subgraph "Capa de Herramientas"
        I[Financial Calculator 🧮]
        J[Legal RAG Retriever ⚖️]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    C --> I
    C --> J
    J --> F
    F --> G
    G --> H
```

## Flujo de Datos

```mermaid
sequenceDiagram
    participant U as Usuario
    participant S as Streamlit
    participant SG as StateGraph
    participant SUP as Supervisor
    participant FC as Financial Calculator
    participant LA as Legal Analyst
    participant LLM as Llama3 (Groq)
    participant VS as Vector Store
    
    U->>S: Mensaje: "Activos 500M, deudas 100M"
    S->>SG: invoke(messages)
    SG->>SUP: Procesar mensaje
    SUP->>LLM: Analizar + System Prompt
    LLM->>SUP: Tool Call: calculate_society_split
    SUP->>FC: Ejecutar cálculo (500, 100)
    FC->>SUP: Resultado: "200M c/u"
    SUP->>LLM: Generar respuesta con resultado
    LLM->>SUP: Respuesta formateada
    SUP->>SG: Actualizar estado
    SG->>S: Devolver respuesta
    S->>U: Mostrar respuesta
    
    Note over U,VS: Cuando hay consulta legal:
    
    U->>S: "¿Qué dice la ley sobre bienes?"
    S->>SG: invoke(messages)
    SG->>SUP: Procesar pregunta
    SUP->>LLM: Analizar
    LLM->>SUP: Tool Call: legal_analyst_tool
    SUP->>LA: Consultar corpus
    LA->>VS: Buscar documentos similares
    VS->>LA: Devolver chunks relevantes
    LA->>SUP: Documentos encontrados
    SUP->>LLM: Generar respuesta con docs
    LLM->>SUP: Respuesta con citas
    SUP->>SG: Actualizar estado
    SG->>S: Devolver respuesta
    S->>U: Mostrar respuesta con citas
```

---

## 📊 Métricas del Sistema

### Componentes Principales
- **1** Supervisor (Mediator_Supervisor_Agent)
- **2** Herramientas especializadas:
  - Financial_Calculator_Agent
  - Legal_Analyst_Agent (RAG)
- **3** Puntos nodales de mediación
- **3** Documentos en corpus legal

### Tecnologías
1. **LangGraph** - Orquestación de agentes
2. **LangChain** - Framework de LLM
3. **Groq** - Inferencia rápida de LLM
4. **Streamlit** - Frontend web
5. **ChromaDB** - Vector database
6. **HuggingFace** - Embeddings
7. **Python-dotenv** - Gestión de configuración
8. **Sentence Transformers** - Modelos de embeddings

### Características
- ✅ Arquitectura modular y extensible
- ✅ RAG sobre corpus legal personalizado
- ✅ Barrera ética de contención
- ✅ Estado persistente de conversación
- ✅ Interfaz intuitiva
- ✅ Respuestas fundamentadas en ley

---

## 🔄 Extensiones Futuras

```mermaid
mindmap
  root((MEDI-IA-LEGAL))
    Herramientas Adicionales
      Calculadora de Pensiones
      Generador de Documentos
      Validador de Acuerdos
    Corpus Expandido
      Jurisprudencia completa
      Doctrina legal
      Casos precedentes
    Multi-idioma
      Inglés
      Portugués
    Integración Judicial
      Firma digital
      Radicación automática
      Seguimiento de casos
    Analytics
      Dashboard de métricas
      Reportes de mediación
      KPIs de equidad
```

---

## 💡 Principios de Diseño

1. **Modularidad**: Cada componente es independiente y reemplazable
2. **Transparencia**: Las decisiones del sistema están fundamentadas y explicadas
3. **Ética**: Barrera activa contra propuestas injustas
4. **Escalabilidad**: Fácil agregar nuevos agentes y herramientas
5. **User-Centric**: Interfaz simple y guía paso a paso

---

*Diagrama generado para MEDI-IA-LEGAL - Sistema de Mediación Inteligente*
