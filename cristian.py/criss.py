
# Lista global de tareas
tareas = []

# FUNCIONES DEL MENU

def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Debe ingresar un numero entre 1 y 6.")
        except ValueError:
            print("Error: Debe ingresar un numero valido.")

# VALIDACIONES

def validar_descripcion(descripcion):
    return descripcion.strip() != ""


def validar_prioridad(prioridad):
    return 1 <= prioridad <= 10


def validar_tiempo(tiempo):
    return tiempo > 0

# OPCION 1

def agregar_tarea(lista):
    descripcion = input("Ingrese descripcion: ")

    if not validar_descripcion(descripcion):
        print("Error: La descripcion no puede estar vacia.")
        return

    try:
        prioridad = int(input("Ingrese prioridad (1-10): "))
    except ValueError:
        print("Error: La prioridad debe ser un numero entero.")
        return

    if not validar_prioridad(prioridad):
        print("Error: La prioridad debe estar entre 1 y 10.")
        return

    try:
        tiempo = float(input("Ingrese tiempo estimado (horas): "))
    except ValueError:
        print("Error: El tiempo estimado debe ser un numero.")
        return

    if not validar_tiempo(tiempo):
        print("Error: El tiempo estimado debe ser mayor que cero.")
        return

    tarea = {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "tiempo_estimado": tiempo,
        "completada": False
    }

    lista.append(tarea)
    print("Tarea registrada correctamente.")



def buscar_tarea(lista, descripcion):
    for i in range(len(lista)):
        if lista[i]["descripcion"] == descripcion:
            return i
    return -1


def actualizar_estado(lista):
    for tarea in lista:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

def mostrar_tareas(lista):
    actualizar_estado(lista)

    print("\n=== LISTA DE TAREAS ===")

    if len(lista) == 0:
        print("No hay tareas registradas.")
        return

    for tarea in lista:
        print(f"Descripcion: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")

        if tarea["completada"]:
            print("Estado: COMPLETADA")
        else:
            print("Estado: PENDIENTE")

        print("*********************************************")

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_tarea(tareas)

    elif opcion == 2:
        descripcion = input("Ingrese descripción a buscar: ")

        posicion = buscar_tarea(tareas, descripcion)

        if posicion != -1:
            tarea = tareas[posicion]

            print("\nTarea encontrada")
            print("Posición:", posicion)
            print("Descripción:", tarea["descripcion"])
            print("Prioridad:", tarea["prioridad"])
            print("Tiempo estimado:", tarea["tiempo_estimado"])
            print("Completada:", tarea["completada"])
        else:
            print("La tarea no existe.")

    elif opcion == 3:
        descripcion = input("Ingrese descripción de la tarea a eliminar: ")

        posicion = buscar_tarea(tareas, descripcion)

        if posicion != -1:
            tareas.pop(posicion)
            print("Tarea eliminada correctamente.")
        else:
            print(f"La tarea '{descripcion}' no se encuentra registrada.")

    elif opcion == 4:
        actualizar_estado(tareas)
        print("Estados actualizados correctamente.")

    elif opcion == 5:
        mostrar_tareas(tareas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break