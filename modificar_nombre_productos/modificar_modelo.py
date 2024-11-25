def procesar_modificacion_modelos(entradas_producto, modelos, modificar_realmente=False):
    """Procesa las modificaciones de modelos y registra los cambios."""
    log_cambios = []

    for entrada in entradas_producto:
        if 'es' in entrada._fields and 'model' in entrada._fields['es']:
            modelo = entrada._fields['es']['model']
            country_code = entrada._fields['es']['country_code']
            entry_id = entrada.sys['id']  # Obtener el ID de la entrada

            if modelo in modelos and country_code == "MX":
                print(f"Modelo encontrado (ID: {entry_id}):", modelo)

                # Quitar año al final del modelo encontrado
                modelo_sin_año = ' '.join(modelo.split()[:-1])

                # Comparar el modelo original con el modelo sin el año
                if modelo_sin_año == modelo:
                    print(f"El modelo ya no contiene año (ID: {entry_id}):", modelo)
                    continue

                # Registrar el cambio en el log
                log_cambios.append({
                    "id": entry_id,
                    "antes": modelo,
                    "después": modelo_sin_año
                })

                if modificar_realmente:
                    # Realizar cambio en el campo 'model'
                    entrada._fields['es']['model'] = modelo_sin_año
                    entrada.save()  # Guardar cambios
                    entrada.publish()
                    print(f"Cambio realizado (ID: {entry_id}): {modelo} -> {modelo_sin_año}")
                else:
                    # Simulación: Mostrar lo que se haría sin modificar
                    print(f"Simulación (ID: {entry_id}): {modelo} -> {modelo_sin_año}")

    return log_cambios