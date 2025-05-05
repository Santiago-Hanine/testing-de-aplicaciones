import re

tareas = []  # Lista de tareas: cada tarea es un diccionario {"texto": str, "completada": bool}

def mostrar_menu():
	print("\nGestión de Tareas")
	print("1. Agregar Tarea")
	print("2. Eliminar Tarea")
	print("3. Ver Tareas")
	print("4. Modificar Tarea")
	print("5. Marcar/Desmarcar como Completada")
	print("6. Salir")

def validar_tarea(tarea):
	if not tarea.strip():
		print("❌ La tarea no puede estar vacía.")
		return False
	if not re.match(r"^[\w\s.,¡!¿?áéíóúÁÉÍÓÚñÑ-]+$", tarea):
		print("❌ La tarea contiene caracteres no permitidos.")
		return False
	return True

def agregar_tarea():
	tarea = input("Ingrese la tarea: ")
	if validar_tarea(tarea):
		tareas.append({"texto": tarea.strip(), "completada": False})
		print(f"✅ Tarea '{tarea}' agregada.")

def eliminar_tarea():
	ver_tareas()
	try:
		indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
		if 0 <= indice < len(tareas):
			eliminada = tareas.pop(indice)
			print(f"🗑️ Tarea '{eliminada['texto']}' eliminada.")
		else:
			print("❌ Número de tarea inválido.")
	except ValueError:
		print("❌ Por favor, ingrese un número válido.")

def ver_tareas():
	if not tareas:
		print("📭 No hay tareas disponibles.")
	else:
		print("\n📋 Tareas:")
		for i, tarea in enumerate(tareas, start=1):
			estado = "[✔]" if tarea["completada"] else "[ ]"
			print(f"{i}. {estado} {tarea['texto']}")

def modificar_tarea():
	ver_tareas()
	try:
		indice = int(input("Ingrese el número de la tarea a modificar: ")) - 1
		if 0 <= indice < len(tareas):
			nueva = input("Ingrese el nuevo texto de la tarea: ")
			if validar_tarea(nueva):
				tareas[indice]["texto"] = nueva.strip()
				print("✏️ Tarea modificada correctamente.")
		else:
			print("❌ Número de tarea inválido.")
	except ValueError:
		print("❌ Por favor, ingrese un número válido.")

def marcar_completada():
	ver_tareas()
	try:
		indice = int(input("Ingrese el número de la tarea a marcar/desmarcar: ")) - 1
		if 0 <= indice < len(tareas):
			tareas[indice]["completada"] = not tareas[indice]["completada"]
			estado = "completada" if tareas[indice]["completada"] else "pendiente"
			print(f"☑️ Tarea marcada como {estado}.")
		else:
			print("❌ Número de tarea inválido.")
	except ValueError:
		print("❌ Por favor, ingrese un número válido.")

def main():
	while True:
		mostrar_menu()
		try:
			opcion = int(input("Elija una opción: "))
			if opcion == 1:
				agregar_tarea()
			elif opcion == 2:
				eliminar_tarea()
			elif opcion == 3:
				ver_tareas()
			elif opcion == 4:
				modificar_tarea()
			elif opcion == 5:
				marcar_completada()
			elif opcion == 6:
				print("👋 Saliendo del programa.")
				break
			else:
				print("❌ Opción inválida. Por favor, intente nuevamente.")
		except ValueError:
			print("❌ Por favor, ingrese un número válido.")

main()
