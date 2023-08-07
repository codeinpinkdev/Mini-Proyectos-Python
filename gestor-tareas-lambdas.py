"""
Gestor de tareas (Con Lambdas): 

Crea un programa que permita al usuario agregar tareas a una lista, marcar tareas como completadas y eliminar tareas de la lista. Puedes usar una lista para almacenar las tareas y funciones para manejar las operaciones de agregar, marcar y eliminar tareas.
"""
agregar_tarea = lambda lista_tareas, tarea: (lista_tareas.append(tarea), print("Tarea agregada:", tarea))

quitar_tarea = lambda lista_tareas, tarea: (lista_tareas.remove(tarea), print("Tarea completada:", tarea)) if tarea in lista_tareas else print("La tarea no está en la lista.")

mostrar_tarea = lambda lista_tareas: print("Tareas pendientes:\n", "\n".join(f"- {t}" for t in lista_tareas))



def tareas():
  lista_tareas = []
  while True:
      print("\n--- Gestor de Tareas ---")
      print("1. Agregar tarea")
      print("2. Marcar tarea como completada")
      print("3. Mostrar tareas pendientes")
      print("4. Salir \n")
  
      opcion = int(input("- Ingrese el número de la opción que desea realizar (1/2/3/4): "))

      if opcion == 1:
        nueva_tarea = input("Dame el nombre de la tarea: ")
        agregar_tarea(lista_tareas, nueva_tarea)
      elif opcion == 2: 
        completar_tarea = input("Tarea a Eliminar: ")
        quitar_tarea(lista_tareas, completar_tarea)
      elif opcion == 3:
         mostrar_tarea(lista_tareas)
      elif opcion == 4:
         break

if __name__ == "__main__":
    tareas()
