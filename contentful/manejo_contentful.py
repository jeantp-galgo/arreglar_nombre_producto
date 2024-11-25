import contentful_management # Manejar Contentful desde el management API
from utilidades.utils import * # Funciones de utilidad
from contentful.utils import * # Funciones de utilidad
import os # Manejar variables de entorno
from dotenv import load_dotenv # Manejar variables de entorno
load_dotenv() # Cargar variables de entorno

# Carga los datos del JSON
token = os.getenv("MANAGEMENT_TOKEN") # Token de acceso 
space_id = os.getenv("SPACE_ID") # ID del espacio
environment_id = os.getenv("ENVIRONMENT") # ID del entorno

class ContentfulManager:
    def __init__(self):
        self.client = contentful_management.Client(token) # Cliente de Contentful
        self.space_id = space_id # ID del espacio
        self.environment_id = environment_id # ID del entorno

    def traer_content_type(self, nombre_content_type, content_types=None):
        """
        Trae un content type y todas sus entradas.
        Args:
            nombre_content_type (str): Nombre del content type.
            content_types (list): Lista de content types.
        Returns:
            tuple: Objeto del content type y todas sus entradas.
        """
        if content_types is None:
            content_types = lista_content_types(self.client, self.space_id, self.environment_id, mostrar=False) # Lista los content type disponibles
        content_type = seleccionar_content_type(content_types, nombre_content_type) # Objeto del content type elejido
        entradas_content_type = mostrar_entradas(self.client, self.space_id, self.environment_id, content_type.id, mostrar=False) # Mostrar todas las entradas del content type
        return content_type, entradas_content_type
    
    def entradas_por_pais(self,content_type_id, country_code, mostrar=True):
        """
        Trae todas las entradas de un content type dado un país.
        Args:
            content_type_id (str): ID del content type.
            country_code (str): Código de país.
            mostrar (bool): Si es True, muestra las entradas en la consola.
        Returns:
            list: Lista de entradas.
        """
        all_entries = []
        skip = 0
        limit = 100  # Límite máximo en Contentful

        while True:
            entries = self.client.entries(self.space_id, self.environment_id).all({
                'content_type': content_type_id,
                'fields.country_code': country_code,
                'skip': skip,
                'limit': limit
            })
            all_entries.extend(entries)
            skip += limit
                
            if len(entries) < limit:
                break  # Finaliza si no hay más entradas
        print(len(all_entries))
        if mostrar:
            mostrar_respuesta(all_entries)
        return all_entries

