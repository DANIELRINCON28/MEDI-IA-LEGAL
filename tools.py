"""
Módulo de Herramientas para MEDI-IA-LEGAL
Contiene los agentes especializados implementados como herramientas de LangChain.
"""

from langchain_core.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools import create_retriever_tool


# ============================================================================
# HERRAMIENTA FINANCIERA: Financial_Calculator_Agent
# ============================================================================

@tool
def calculate_society_split(total_assets: float, total_debts: float) -> str:
    """
    Calcula la división de la sociedad conyugal según la ley colombiana.
    
    Args:
        total_assets: Valor total de los activos de la sociedad conyugal en millones de pesos.
        total_debts: Valor total de las deudas de la sociedad conyugal en millones de pesos.
    
    Returns:
        str: Explicación detallada del cálculo de la división 50/50.
    """
    # Calcular el valor neto
    net_value = total_assets - total_debts
    
    # Calcular la porción del 50% para cada cónyuge
    spouse_share = net_value / 2
    
    # Formatear el resultado
    result = f"""
📊 CÁLCULO DE LIQUIDACIÓN DE SOCIEDAD CONYUGAL

🔹 Total de Activos: ${total_assets:,.2f} millones COP
🔹 Total de Deudas: ${total_debts:,.2f} millones COP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔹 Valor Neto: ${net_value:,.2f} millones COP

⚖️ DIVISIÓN EQUITATIVA (50/50 según Código Civil):
   • Cónyuge 1: ${spouse_share:,.2f} millones COP
   • Cónyuge 2: ${spouse_share:,.2f} millones COP

💡 Este cálculo se basa en el principio de división igualitaria establecido 
   en el Código Civil Colombiano para la sociedad conyugal.
"""
    
    return result.strip()


# ============================================================================
# HERRAMIENTA LEGAL: Legal_Analyst_Agent (RAG)
# ============================================================================

def setup_legal_rag_tool():
    """
    Configura la herramienta RAG del Legal Analyst Agent.
    Carga el corpus legal simulado y crea un retriever.
    
    Returns:
        Tool: Herramienta de retrieval sobre el corpus jurídico.
    """
    # 1. Cargar documentos de la carpeta corpus/
    loader = DirectoryLoader(
        path="corpus/",
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    documents = loader.load()
    
    # 2. Dividir los documentos en chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    splits = text_splitter.split_documents(documents)
    
    # 3. Inicializar los embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    # 4. Crear Chroma Vectorstore en memoria
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        collection_name="legal_corpus"
    )
    
    # 5. Convertir a retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}  # Devolver los 3 documentos más relevantes
    )
    
    # 6. Crear la herramienta de retrieval
    legal_analyst_tool = create_retriever_tool(
        retriever=retriever,
        name="legal_analyst_tool",
        description=(
            "Consulta el corpus jurídico colombiano (Ley 2442 de 2024, Código Civil) "
            "para responder preguntas sobre los fundamentos legales del divorcio, "
            "la división de bienes y las obligaciones sobre hijos menores. "
            "Usa esta herramienta cuando necesites citar leyes o verificar la legalidad "
            "de una propuesta."
        )
    )
    
    return legal_analyst_tool
