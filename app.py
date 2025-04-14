tareas = []

def mostrar_menu():
	print("\nGestión de Tareas")
	print("1. Agregar Tarea")
	print("2. Eliminar Tarea")
	print("3. Ver Tareas")
	print("4. Salir")

def agregar_tarea():
	tarea = input("Ingrese la tarea: ")
	tareas.append(tarea)
	print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea():
	ver_tareas()
	try:
		indice_tarea = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
		if 0 <= indice_tarea < len(tareas):
			tarea_eliminada = tareas.pop(indice_tarea)
			print(f"Tarea '{tarea_eliminada}' eliminada.")
		else:
			print("Número de tarea inválido.")
	except ValueError:
		print("Por favor, ingrese un número válido.")

def ver_tareas():
	if not tareas:
		print("No hay tareas disponibles.")
	else:
		print("\nTareas:")
		for i, tarea in enumerate(tareas, start=1):
			print(f"{i}. {tarea}")

def main():
	opcion = ""
	while opcion != -1:
		mostrar_menu()
		try:
			opcion = int(input("Elija una opción: (-1 para salir) "))
			if opcion == 1:
				agregar_tarea()
			elif opcion == 2:
				eliminar_tarea()
			elif opcion == 3:
				ver_tareas()
			elif opcion == -1:
				print("Saliendo del programa.")
			else:
				print("Opción inválida. Por favor, intente nuevamente.")
		except ValueError:
			print("Por favor, ingrese un número válido.")

main()