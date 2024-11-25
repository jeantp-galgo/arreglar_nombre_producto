import os

class carpeta:

    # Creación de carpetas
    def crear(ruta):
        os.makedirs(ruta, exist_ok=True)
        if os.path.exists(ruta):
            print(f"La carpeta '{ruta}' se creó correctamente.")
            return True
        else:
            print(f"Error al crear la carpeta '{ruta}'.")
            return None
        
    # Saber si existe una carpeta local 
    def existe(ruta):
        if os.path.exists(ruta):
            print(f"La carpeta si existe")
            return True
        else:
            print(f"La carpeta no existe")
            return None

    # Permite leer la ruta de los archivos dentro de la carpeta
    def extraer_ruta_archivos(ruta_carpeta):
        archivos = []
        for nombre_archivo in os.listdir(ruta_carpeta):
            ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
            # Comprobar que sea un archivo (y no una subcarpeta)
            if os.path.isfile(ruta_archivo):
                archivos.append(ruta_archivo)
        return archivos