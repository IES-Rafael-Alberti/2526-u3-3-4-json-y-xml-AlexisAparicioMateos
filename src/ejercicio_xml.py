import xml.etree.ElementTree as ET

def inicializar_datos():

    """
    Copia el contenido del archivo origen (datos_usuarios_orig.xml)
    a otro archivo destino (datos_usuarios.xml)
    """
    arbol = ET.parse("datos_usuarios_orig.xml")
    raiz = arbol.getroot()

    arbol.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)

def mostrar_datos():
    """
    Muestra de forma organizada el contenido del archivo XML.
    """
    arbol = ET.parse("datos_usuarios.xml")
    raiz = arbol.getroot()

    print("--- Contenido Actual del XML ---")

    for usuario in raiz.findall("usuario"):
        id_ = usuario.find("id").text
        nombre = usuario.find("nombre").text
        edad = usuario.find("edad").text

        print(f"ID: {id_}, Nombre: {nombre}, Edad: {edad}")

    print("--- Fin del Contenido ---\n")

def actualizar_edad(id_usuario):
    """
    Actualiza la edad de uno de los usuarios del archivo xml
    sumandole 1 año a su edad.
    """
    arbol = ET.parse("datos_usuarios.xml")
    raiz = arbol.getroot()

    for usuario in raiz.findall("usuario"):
        id_actual = usuario.find("id").text

        if id_actual == str(id_usuario):
            edad = usuario.find("edad")
            edad.text = str(int(edad.text) + 1)

            arbol.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)
            print(f"\nUsuario con ID {id_usuario} actualizado.\n")
            return

    print(f"No se encontró un usuario con ID {id_usuario}.")

def añadir_usuario(id_nuevo, nombre_nuevo, edad_nueva):
    """
    Añade un usuario a la lista xml sobreescribiéndola.
    """
    arbol = ET.parse("datos_usuarios.xml")
    raiz = arbol.getroot()

    nuevo_usuario = ET.Element("usuario")

    id_elem = ET.SubElement(nuevo_usuario, "id")
    id_elem.text = str(id_nuevo)

    nombre_elem = ET.SubElement(nuevo_usuario, "nombre")
    nombre_elem.text = nombre_nuevo

    edad_elem = ET.SubElement(nuevo_usuario, "edad")
    edad_elem.text = str(edad_nueva)

    raiz.append(nuevo_usuario)

    arbol.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)
    print(f"\nUsuario con ID {id_nuevo} añadido.\n")
    return

def eliminar_usuario(id_usuario):
    """
    Elimina un usuario de la lista
    """
    arbol = ET.parse("datos_usuarios.xml")
    raiz = arbol.getroot()

    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            raiz.remove(usuario)
            print(f"\nUsuario con ID {id_usuario} eliminado.\n")
            break
    else:
        print(f"No se encontró usuario con ID {id_usuario}")

    arbol.write("datos_usuarios.xml", encoding="utf-8", xml_declaration=True)

def main():

    inicializar_datos()
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    actualizar_edad(2)
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    añadir_usuario(3,"Pablo", 45)
    mostrar_datos()
    input("Presiona cualquier tecla para continuar: ")
    eliminar_usuario(1)
    mostrar_datos()
    print("Programa finalizado.")

if __name__ == "__main__":
    main()