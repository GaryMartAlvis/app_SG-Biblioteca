from biblioteca.biblioteca import Biblioteca
from biblioteca.menu import mostrar_menu

def main():
    """
    Función principal que ejecuta el programa de la biblioteca.
    """
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            descripcion = input("Descripción del libro: ")
            biblioteca.agregar_libro(titulo, autor, descripcion)
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            titulo = input("Título del libro: ")
            biblioteca.mostrar_descripcion_libro(titulo)
        elif opcion == "4":
            titulo = input("Título del libro: ")
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.prestar_libro(titulo, nombre_usuario)
        elif opcion == "5":
            titulo = input("Título del libro: ")
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.devolver_libro(titulo, nombre_usuario)
        elif opcion == "6":
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)
        elif opcion == "7":
            biblioteca.listar_usuarios()
        elif opcion == "8":
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.listar_libros_usuario(nombre_usuario)
        elif opcion == "9":
            biblioteca.guardar_datos()
            print("Datos guardados correctamente.")
        elif opcion == "10":
            biblioteca.cargar_datos()
            print("Datos cargados correctamente.")
        elif opcion == "0":
            biblioteca.guardar_datos()
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()