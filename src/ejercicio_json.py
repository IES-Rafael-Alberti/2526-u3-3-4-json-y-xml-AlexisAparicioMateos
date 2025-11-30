import json
import os

def inicializar_datos():
    """
    Copia el contenido del archivo origen (datos_usuarios_orig.json)
    a otro archivo destino (datos_usuarios.json)
    """

    archivo_origen = "datos_usuarios_orig.json"
    archivo_destino = "datos_usuarios.json"

    # 1. Verificar si el archivo origen existe
    if not os.path.exists(archivo_origen):
        print(f"ERROR El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
        return

    # 2. Intentar abrir y cargar el JSON origen
    try:
        with open(archivo_origen, "r") as archivo:
            datos = json.load(archivo)
    except json.JSONDecodeError:
        print(f"ERROR El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")
        return

    # 3. Verificar si el archivo contiene usuarios
    if "usuarios" not in datos or not isinstance(datos["usuarios"], list) or len(datos["usuarios"]) == 0:
        print("ERROR El archivo JSON no contiene usuarios!")
        return

    # 4. Copiar el contenido al archivo destino
    with open(archivo_destino, "w") as archivo:
        json.dump(datos, archivo, indent=4)

    print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")

def mostrar_datos():
    """
    Muestra de forma organizada el contenido del archivo JSON.
    """
    with open("datos_usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    print("\n--- Contenido Actual del JSON ---")
    for usuario in datos["usuarios"]:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")

    print('--- Fin del Contenido ---\n')

def actualizar_edad():
    """
    Actualiza la edad de uno de los usuarios del archivo json
    sumandole 1 año a su edad.
    """

    with open("datos_usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    datos["usuarios"][1]["edad"] +=1

    with open("datos_usuarios.json", "w") as archivo:
        json.dump(datos,archivo, indent=4)

    print("\nUsuario con ID 2 actualizado.")

def añadir_usuario():
    """
    Añade un usuario a la lista json sobreescribiéndola.
    """

    with open("datos_usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    datos["usuarios"].append({"id": 3,"nombre": "Fernando","edad": 55})

    with open("datos_usuarios.json", "w") as archivo:
        json.dump(datos,archivo, indent=4)

    print("\nUsuario Fernando añadido.")

def eliminar_usuario():
    """
    Elimina un usuario de la lista
    """

    with open("datos_usuarios.json", "r") as archivo:
        datos = json.load(archivo)

    datos["usuarios"].pop(0)

    with open("datos_usuarios.json", "w") as archivo:
        json.dump(datos,archivo, indent=4)

    print("\nUsuario Juan eliminado.")

def main():

    inicializar_datos()
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    actualizar_edad()
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    añadir_usuario()
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    eliminar_usuario()
    mostrar_datos()
    print("Programa finalizado.")

if __name__ == "__main__":
    main()
