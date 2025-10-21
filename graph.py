"""
Grafo de Mediación MEDI-IA-LEGAL
Implementa la arquitectura de Supervisor con LangGraph.
"""

from typing import Literal
from dotenv import load_dotenv
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from tools import calculate_society_split, setup_legal_rag_tool

# Cargar variables de entorno
load_dotenv()

# ============================================================================
# DEFINICIÓN DEL ESTADO
# ============================================================================

class GraphState(MessagesState):
    """Estado del grafo que gestiona el historial de mensajes."""
    pass


# ============================================================================
# INICIALIZACIÓN DE HERRAMIENTAS Y LLM
# ============================================================================

# Configurar la herramienta RAG
legal_rag_tool = setup_legal_rag_tool()

# Lista de todas las herramientas disponibles
tools = [calculate_society_split, legal_rag_tool]

# Inicializar el LLM (Groq con modelo actualizado)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=2000
)

# Vincular las herramientas al LLM
model_with_tools = llm.bind_tools(tools)


# ============================================================================
# PROMPT DEL SUPERVISOR
# ============================================================================

SUPERVISOR_SYSTEM_PROMPT = """
Eres 'MEDI-IA-LEGAL', un mediador de IA neutral y objetivo. Tu propósito es ayudar a dos cónyuges a co-crear una 'propuesta de divorcio' justa bajo la ley colombiana.

Tu rol es el de ORQUESTADOR. Debes guiar la conversación secuencialmente a través de los 3 Puntos Nodales:
1. Liquidación de la Sociedad Conyugal (Bienes).
2. Obligaciones Alimentarias.
3. Acuerdos sobre Hijos Menores (Custodia, Visitas, Alimentos).

Tienes dos herramientas:
- 'legal_analyst_tool': Para consultar información legal objetiva del corpus jurídico colombiano.
- 'calculate_society_split': Para cálculos financieros precisos de la división de bienes.

**BARRERA ÉTICA DE CONTENCIÓN (Instrucción CRÍTICA):**
Debes velar por la equidad y la ley. Si una de las partes hace una propuesta que parece manifiestamente injusta o contraria a la ley (ej. "Quiero el 80% de los bienes" o "No pagaré alimentos para mis hijos"), DEBES intervenir.
En ese caso, no aceptes la propuesta. En lugar de eso, debes:
1. Señalar la inequidad ("He notado que esta propuesta se desvía de la norma legal...").
2. Invocar al 'legal_analyst_tool' para citar la ley relevante (ej. "La ley establece una división del 50/50 de los bienes...").
3. Pedir a las partes que reconsideren su propuesta.

**Flujo de la Mediación:**
1. Da la bienvenida y establece la agenda (los 3 puntos).
2. Aborda el primer punto (Bienes). Pide a las partes sus datos (total de activos y deudas).
3. Usa 'calculate_society_split' para obtener un cálculo objetivo.
4. Facilita el acuerdo sobre el Punto 1.
5. Avanza al Punto 2 (Alimentos) y luego al Punto 3 (Hijos), usando 'legal_analyst_tool' según sea necesario.
6. Cuando los 3 puntos estén acordados, genera un resumen final y termina la conversación.

Recuerda: Eres neutral, empático, pero firme en la aplicación de la ley. Tu objetivo es un acuerdo justo y legal.
"""


# ============================================================================
# NODO SUPERVISOR
# ============================================================================

def supervisor_node(state: GraphState) -> GraphState:
    """
    Nodo principal del supervisor que orquesta la mediación.
    
    Args:
        state: Estado actual del grafo con el historial de mensajes.
    
    Returns:
        GraphState: Estado actualizado con la respuesta del supervisor.
    """
    # Obtener los mensajes actuales
    messages = state["messages"]
    
    # Si es el primer mensaje, añadir el system prompt
    if len(messages) == 1:  # Solo hay el mensaje del usuario
        messages_with_system = [
            SystemMessage(content=SUPERVISOR_SYSTEM_PROMPT),
            *messages
        ]
    else:
        # Verificar si ya existe el system message
        if not any(isinstance(msg, SystemMessage) for msg in messages):
            messages_with_system = [
                SystemMessage(content=SUPERVISOR_SYSTEM_PROMPT),
                *messages
            ]
        else:
            messages_with_system = messages
    
    # Invocar al modelo con las herramientas
    response = model_with_tools.invoke(messages_with_system)
    
    # Devolver el estado actualizado
    return {"messages": [response]}


# ============================================================================
# FUNCIÓN DE ENRUTAMIENTO
# ============================================================================

def router(state: GraphState) -> Literal["tools", "__end__"]:
    """
    Determina si el supervisor necesita usar herramientas o terminar.
    
    Args:
        state: Estado actual del grafo.
    
    Returns:
        str: "tools" si hay tool_calls, END si no.
    """
    last_message = state["messages"][-1]
    
    # Si el último mensaje tiene tool_calls, ir a las herramientas
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    
    # De lo contrario, continuar la conversación (no terminar automáticamente)
    return "__end__"


# ============================================================================
# CONSTRUCCIÓN DEL GRAFO
# ============================================================================

# Crear el grafo
workflow = StateGraph(GraphState)

# Añadir nodos
workflow.add_node("supervisor", supervisor_node)
tool_node = ToolNode(tools)
workflow.add_node("tools", tool_node)

# Establecer el punto de entrada
workflow.set_entry_point("supervisor")

# Añadir aristas condicionales desde el supervisor
workflow.add_conditional_edges(
    "supervisor",
    router,
    {
        "tools": "tools",
        "__end__": END
    }
)

# Conectar las herramientas de vuelta al supervisor
workflow.add_edge("tools", "supervisor")

# Compilar el grafo
mediation_graph = workflow.compile()
