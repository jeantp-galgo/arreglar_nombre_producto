from datetime import datetime
import re

def obtener_fecha_hora_actual():
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    # Formatear la fecha y hora como string
    fecha_hora_str = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    return fecha_hora_str

# --- CONTENTFUL ---
def mostrar_respuesta(array_respuesta):
    for respuesta in array_respuesta:
        print(respuesta)

def extraer_numero(texto):
    # Buscar el primer número en el texto, que puede incluir decimales
    resultado = re.search(r"\d+(\.\d+)?", texto)
    if resultado:
        return float(resultado.group()) if '.' in resultado.group() else int(resultado.group())
    return None  # Retorna None si no se encuentra un número