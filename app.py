"""
Interfaz de Usuario con Streamlit para MEDI-IA-LEGAL
"""

import streamlit as st
from graph import mediation_graph

# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="MEDI-IA-LEGAL",
    page_icon="⚖️",
    layout="wide"
)

# ============================================================================
# TÍTULO Y DESCRIPCIÓN
# ============================================================================

st.title("⚖️ MEDI-IA-LEGAL: Mediación de Divorcio Asistida por IA")
st.caption("Prototipo basado en LangGraph y la Ley 2442 de 2024")

st.markdown("""
---
**Sistema de Mediación Inteligente** para propuestas de divorcio unilateral en Colombia.  
Este asistente te guiará a través de los 3 puntos nodales:
1. 💰 Liquidación de la Sociedad Conyugal
2. 💵 Obligaciones Alimentarias  
3. 👨‍👩‍👧‍👦 Acuerdos sobre Hijos Menores

*El sistema vela por la equidad y el cumplimiento de la ley colombiana.*
---
""")

# ============================================================================
# INICIALIZACIÓN DEL ESTADO DE LA SESIÓN
# ============================================================================

# Configuración del thread para LangGraph
if "config" not in st.session_state:
    st.session_state.config = {
        "configurable": {
            "thread_id": "demo_thread"
        }
    }

# Inicializar el historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # Mensaje de bienvenida automático
    with st.spinner("🤖 MEDI-IA-LEGAL se está iniciando..."):
        try:
            # Invocar el grafo con un mensaje de inicio
            initial_message = "Hola, estoy listo para comenzar la mediación."
            response = mediation_graph.invoke(
                {"messages": [("user", initial_message)]},
                config=st.session_state.config
            )
            
            # Extraer la respuesta de la IA
            if response and "messages" in response and len(response["messages"]) > 0:
                ai_message = response["messages"][-1]
                if hasattr(ai_message, "content"):
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": ai_message.content
                    })
        except Exception as e:
            st.error(f"Error al inicializar: {str(e)}")
            st.info("💡 Asegúrate de haber configurado tu GROQ_API_KEY en el archivo .env")

# ============================================================================
# MOSTRAR HISTORIAL DE CHAT
# ============================================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================================================
# ENTRADA DEL USUARIO
# ============================================================================

if prompt := st.chat_input("Escribe tu propuesta o respuesta..."):
    # Añadir mensaje del usuario al historial
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        with st.spinner("🤖 MEDI-IA-LEGAL está analizando..."):
            try:
                # Invocar el grafo
                response = mediation_graph.invoke(
                    {"messages": [("user", prompt)]},
                    config=st.session_state.config
                )
                
                # Extraer la respuesta de la IA
                if response and "messages" in response:
                    ai_message = response["messages"][-1]
                    
                    # Verificar si es un mensaje de contenido o una llamada a herramientas
                    if hasattr(ai_message, "content") and ai_message.content:
                        ai_response = ai_message.content
                    else:
                        # Si hay tool_calls, esperar a que se ejecuten
                        # El grafo debería manejar esto automáticamente
                        ai_response = "Procesando información..."
                    
                    # Mostrar la respuesta
                    st.markdown(ai_response)
                    
                    # Añadir al historial
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": ai_response
                    })
                else:
                    st.error("No se recibió respuesta del sistema.")
                    
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })

# ============================================================================
# SIDEBAR CON INFORMACIÓN
# ============================================================================

with st.sidebar:
    st.header("📋 Información del Sistema")
    
    st.markdown("""
    ### 🎯 Objetivo
    Facilitar la co-creación de una propuesta de divorcio justa y legal.
    
    ### 🛠️ Herramientas Disponibles
    - **Legal Analyst**: Consulta el corpus jurídico
    - **Financial Calculator**: Cálculos de división de bienes
    
    ### ⚖️ Barrera Ética
    El sistema rechazará propuestas injustas o ilegales.
    
    ### 📚 Base Legal
    - Ley 2442 de 2024
    - Código Civil Colombiano
    - Interés Superior del Menor
    """)
    
    st.divider()
    
    if st.button("🔄 Reiniciar Conversación"):
        st.session_state.messages = []
        st.session_state.config = {
            "configurable": {
                "thread_id": f"demo_thread_{len(st.session_state.messages)}"
            }
        }
        st.rerun()
    
    st.divider()
    st.caption("Desarrollado con LangGraph + Streamlit")
