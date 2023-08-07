"""
Gestor de tareas: 

Crea un programa que permita al usuario agregar tareas a una lista, marcar tareas como completadas y eliminar tareas de la lista. Puedes usar una lista para almacenar las tareas y funciones para manejar las operaciones de agregar, marcar y eliminar tareas.
"""

def agregar_tarea(lista_tareas, tarea):
  lista_tareas.append(tarea)
  print("\n------")
  print("La tarea agregada fue: ", tarea)
  print("------")

def quitar_tarea(lista_tareas, tarea):
  if tarea in lista_tareas:
    lista_tareas.remove(tarea)
    print("\n------")
    print("La tarea :", tarea, "fue completada, se quitará de la lista con éxito")
    print("------")

def mostrar_tarea(lista_tareas):
  print("\n------")
  print("Tareas pendientes:")
  for tarea in lista_tareas:
    print("*", tarea)
  print("------")

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
