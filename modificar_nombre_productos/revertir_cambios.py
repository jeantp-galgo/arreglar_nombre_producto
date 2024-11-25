import json

def revertir_todos_cambios(json_path, entradas_producto):
    """
    Revertir los cambios realizados para todas las entradas registradas en el archivo JSON,
    si el nombre actual del modelo es diferente al nombre original registrado.
    
    Args:
        json_path (str): Ruta al archivo JSON que contiene el log de cambios.
        entradas_producto (list): Lista de entradas cargadas desde Contentful.
    """
    try:
        # Leer el JSON con los cambios realizados
        with open(json_path, "r", encoding="utf-8") as archivo:
            log_cambios = json.load(archivo)
        
        cambios_revertidos = 0
        for cambio in log_cambios:
            id_entrada = cambio["id"]
            nombre_anterior = cambio["antes"]
            nombre_modificado = cambio["después"]
            
            # Buscar la entrada en las entradas consultadas
            entrada_objetivo = next((entrada for entrada in entradas_producto if entrada.sys["id"] == id_entrada), None)
            
            if not entrada_objetivo:
                print(f"No se encontró la entrada con ID {id_entrada}. Saltando...")
                continue
            
            # Obtener el modelo actual desde la entrada
            modelo_actual = entrada_objetivo._fields["es"]["model"]
            
            if modelo_actual == nombre_anterior:
                print(f"El modelo actual ya coincide con el original (ID: {id_entrada}). Saltando...")
                continue
            
            # Revertir el nombre del modelo
            entrada_objetivo._fields["es"]["model"] = nombre_anterior
            
            # Guardar los cambios
            entrada_objetivo.save()

            # Publicar cambios realizados
            #entrada_objetivo.publish()

            print(f"Cambio revertido (ID: {id_entrada}): Modelo ahora es {nombre_anterior}")
            cambios_revertidos += 1

        if cambios_revertidos == 0:
            print("No se realizó ninguna reversión, revisa si las entradas cargadas ya están revertidas o no coinciden con el log.")
        else:
            print(f"Reversión completa: Se revirtieron {cambios_revertidos} cambios.")
    
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {json_path}.")
    except Exception as e:
        print(f"Ocurrió un error al intentar revertir los cambios: {e}")
