from datetime import datetime
import json

def obtener_fecha_actual():
    """Obtiene la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")

def registrar_cambios(log_cambios, fecha_actual):
    """Guarda los cambios en un archivo JSON."""
    if not log_cambios:
        print("No se realizaron cambios en esta ejecución.")
        return

    nombre_archivo_log = f"log_cambios_modelos_{fecha_actual}.json"

    # Convertir los cambios a una lista de diccionarios
    log_lista = [
        {
            "id": cambio['id'],
            "nombre_modelo_modificado": cambio['después'],
            "antes": cambio['antes'],
            "después": cambio['después']
        }
        for cambio in log_cambios
    ]

    # Guardar la lista en un archivo JSON
    with open(nombre_archivo_log, "w", encoding="utf-8") as archivo:
        json.dump(log_lista, archivo, ensure_ascii=False, indent=4)

    print(f"Log guardado en {nombre_archivo_log}")