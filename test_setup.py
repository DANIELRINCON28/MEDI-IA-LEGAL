"""
Script de prueba para verificar la instalación de MEDI-IA-LEGAL
Ejecuta: python test_setup.py
"""

import sys
import os

def test_python_version():
    """Verifica la versión de Python"""
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✓ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"   ✗ Python {version.major}.{version.minor}.{version.micro} (Se requiere Python 3.8+)")
        return False

def test_imports():
    """Verifica que todas las librerías estén instaladas"""
    print("\n📦 Verificando dependencias...")
    
    required_modules = [
        ("langchain", "LangChain"),
        ("langgraph", "LangGraph"),
        ("langchain_groq", "LangChain-Groq"),
        ("streamlit", "Streamlit"),
        ("dotenv", "python-dotenv"),
        ("chromadb", "ChromaDB"),
        ("sentence_transformers", "sentence-transformers"),
    ]
    
    all_ok = True
    for module_name, display_name in required_modules:
        try:
            __import__(module_name)
            print(f"   ✓ {display_name}")
        except ImportError:
            print(f"   ✗ {display_name} (NO INSTALADO)")
            all_ok = False
    
    return all_ok

def test_env_file():
    """Verifica que el archivo .env existe y está configurado"""
    print("\n🔑 Verificando archivo .env...")
    
    if not os.path.exists(".env"):
        print("   ✗ Archivo .env no encontrado")
        return False
    
    with open(".env", "r", encoding="utf-8") as f:
        content = f.read()
    
    if "GROQ_API_KEY" not in content:
        print("   ✗ GROQ_API_KEY no encontrada en .env")
        return False
    
    if 'GROQ_API_KEY="tu_api_key_de_groq"' in content:
        print("   ⚠ GROQ_API_KEY aún no está configurada (usa el valor por defecto)")
        print("     Configúrala antes de ejecutar la aplicación")
        return False
    
    print("   ✓ Archivo .env configurado")
    return True

def test_corpus():
    """Verifica que el corpus legal existe"""
    print("\n📚 Verificando corpus legal...")
    
    corpus_files = [
        "corpus/ley_2442.txt",
        "corpus/codigo_civil.txt",
        "corpus/interes_menor.txt"
    ]
    
    all_ok = True
    for file_path in corpus_files:
        if os.path.exists(file_path):
            print(f"   ✓ {file_path}")
        else:
            print(f"   ✗ {file_path} (NO ENCONTRADO)")
            all_ok = False
    
    return all_ok

def test_main_files():
    """Verifica que los archivos principales del proyecto existen"""
    print("\n📄 Verificando archivos del proyecto...")
    
    main_files = [
        "tools.py",
        "graph.py",
        "app.py",
        "requirements.txt"
    ]
    
    all_ok = True
    for file_path in main_files:
        if os.path.exists(file_path):
            print(f"   ✓ {file_path}")
        else:
            print(f"   ✗ {file_path} (NO ENCONTRADO)")
            all_ok = False
    
    return all_ok

def test_tools_functionality():
    """Prueba básica de las herramientas"""
    print("\n🔧 Probando herramientas...")
    
    try:
        from tools import calculate_society_split
        result = calculate_society_split(500, 100)
        if "200" in result and "50/50" in result:
            print("   ✓ Financial Calculator funciona correctamente")
            return True
        else:
            print("   ✗ Financial Calculator devuelve resultado inesperado")
            return False
    except Exception as e:
        print(f"   ✗ Error al probar herramientas: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("  MEDI-IA-LEGAL - Test de Configuración")
    print("=" * 60)
    
    results = []
    
    results.append(("Python", test_python_version()))
    results.append(("Dependencias", test_imports()))
    results.append(("Archivo .env", test_env_file()))
    results.append(("Corpus Legal", test_corpus()))
    results.append(("Archivos Principales", test_main_files()))
    
    # Solo probar herramientas si las dependencias están instaladas
    if results[1][1]:  # Si dependencias OK
        results.append(("Herramientas", test_tools_functionality()))
    
    print("\n" + "=" * 60)
    print("  RESUMEN")
    print("=" * 60)
    
    for name, status in results:
        status_text = "✓ OK" if status else "✗ FALLO"
        print(f"  {name:.<30} {status_text}")
    
    all_passed = all(status for _, status in results)
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 ¡Todos los tests pasaron! El sistema está listo.")
        print("\nPara ejecutar la aplicación:")
        print("  1. Asegúrate de que GROQ_API_KEY esté configurada en .env")
        print("  2. Ejecuta: streamlit run app.py")
    else:
        print("\n⚠ Algunos tests fallaron. Revisa los errores arriba.")
        print("\nSugerencias:")
        print("  - Ejecuta: pip install -r requirements.txt")
        print("  - Verifica que todos los archivos estén presentes")
        print("  - Configura tu GROQ_API_KEY en .env")
    
    print()

if __name__ == "__main__":
    main()
