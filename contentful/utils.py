from utilidades.utils import *

def lista_content_types(client, space_id, environment_id, mostrar=True):
    content_types = client.content_types(space_id, environment_id).all()
    if mostrar:
        mostrar_respuesta(content_types)
    return content_types

def seleccionar_content_type(content_types, nombre_content_type):
    for content_type in content_types:
        if content_type.id == nombre_content_type:
            print(f"Content type seleccionado: {content_type.id}")
            return content_type

def ver_entrada(client, space_id, environment_id, id_entrada):
    entry = client.entries(space_id, environment_id).find(id_entrada)
    print(entry.fields("es"))
    return entry

def mostrar_entradas(client, space_id, environment_id, content_type_id, mostrar = True):
        all_entries = []
        skip = 0
        limit = 100  # Límite máximo en Contentful

        while True:
            entries = client.entries(space_id, environment_id).all({
                'content_type': content_type_id,
                'skip': skip,
                'limit': limit
            })
            
            all_entries.extend(entries)
            skip += limit

            if len(entries) < limit:
                break  # Finaliza si no hay más entradas

        if mostrar:
            print(len(all_entries))
            mostrar_respuesta(all_entries)

        return all_entries