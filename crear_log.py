import os
from datetime import datetime

def crear_log():
    # 1. Preguntar solo los datos clave (sin pedir el texto largo)
    modelo = input("¿Qué modelo usaste? (Claude/ChatGPT): ").strip()
    tema = input("¿Cuál es el tema de la charla?: ").strip()

    # 2. Preparar el nombre del archivo y la carpeta
    fecha = datetime.now().strftime("%Y-%m-%d")
    carpeta = f"{modelo.lower()}_conversations"
    nombre_archivo = f"{fecha}_{tema.replace(' ', '-')}.md"
    
    # Asegurar que la carpeta exista
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # 3. Crear el formato del archivo con un marcador
    texto_completo = f"""---
fecha: {fecha}
modelo: {modelo}
tema: {tema}
---

# {tema}

[PEGA AQUÍ TU CHARLA]
"""

    # 4. Guardar el archivo
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(texto_completo)
    
    print(f"\n¡Éxito! Archivo creado en: {ruta_completa}")
    print("Abre el archivo en VS Code y reemplaza '[PEGA AQUÍ TU CHARLA]' con tu texto.")

if __name__ == "__main__":
    crear_log()