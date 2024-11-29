import os

def obtener_estructura_directorio(ruta_directorio, nivel=0, ignorar=None):
    if ignorar is None:
        ignorar = set(['env'])
    else:
        ignorar = set(ignorar) | set(['env'])

    estructura = ""
    try:
        archivos_y_directorios = sorted(os.listdir(ruta_directorio))
    except PermissionError:
        return estructura + "    " * nivel + "|-- [Error: Permiso denegado]\n"
    except FileNotFoundError:
        return estructura + "    " * nivel + "|-- [Error: Directorio no encontrado]\n"
    
    for elemento in archivos_y_directorios:
        if elemento in ignorar:
            continue
        ruta_elemento = os.path.join(ruta_directorio, elemento)
        estructura += "    " * nivel + "|-- " + elemento + "\n"
        
        if os.path.isdir(ruta_elemento):
            estructura += obtener_estructura_directorio(ruta_elemento, nivel + 1, ignorar)
    
    return estructura

def imprimir_estructura_proyecto(ruta_proyecto, ignorar=None):
    estructura = obtener_estructura_directorio(ruta_proyecto, ignorar=ignorar)
    print(estructura)
    return estructura

if __name__ == "__main__":
    ruta_proyecto = "/home/makabrus/Workspace/AnalisisEconomico"
    # Puedes añadir más carpetas para ignorar en esta lista
    ignorar = ['env', '.git', '__pycache__']
    estructura = imprimir_estructura_proyecto(ruta_proyecto, ignorar)
    try:
        with open(os.path.join(ruta_proyecto, "estructura_proyecto.txt"), "w", encoding="utf-8") as archivo:
            archivo.write(estructura)
        print(f"La estructura del proyecto se ha guardado en {os.path.join(ruta_proyecto, 'estructura_proyecto.txt')}")
    except PermissionError:
        print("Error: No se pudo escribir el archivo. Permiso denegado.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")