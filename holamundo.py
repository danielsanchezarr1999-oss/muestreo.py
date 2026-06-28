def gestor_tareas():
    tareas_pendientes = ["Configurar entorno", "Crear Base de Datos", "Testeo Unitario"]
    activo = True

    while activo:
        print("\n--- GESTOR DE PROYECTOS DSI ---")
        print("1. Ver lista de tareas (Ciclo FOR)")
        print("2. Agregar nueva tarea")
        print("3. Salir del sistema (Ciclo WHILE)")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\nListado de tareas actuales:")
            # Ciclo FOR para recorrer y enumerar la lista
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"ID {i}: {tarea} - [PENDIENTE]")
        
        elif opcion == "2":
            nueva = input("Nombre de la nueva tarea: ")
            tareas_pendientes.append(nueva)
            print(f"Tarea '{nueva}' añadida con éxito.")
            
        elif opcion == "3":
            print("Finalizando sesión de trabajo...")
            activo = False # Rompe el ciclo while
            
        else:
            print("Error: Entrada no válida.")

if __name__ == "__main__":
    gestor_tareas()