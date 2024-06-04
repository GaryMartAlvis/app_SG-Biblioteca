

def main():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título del libro: ")