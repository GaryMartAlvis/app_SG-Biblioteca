import curses
from biblioteca.biblioteca import Biblioteca
from biblioteca.bienvenida import bienvenida
from biblioteca.menu import draw_menu
from biblioteca.input_handler import get_input
from biblioteca.content_handler import draw_content

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()

    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    current_row_idx = 0
    menu = [
        '01. Agregar libro', '02. Mostrar libros', '03. Mostrar descripción', '04. Prestar libro',
        '05. Devolver libro', '06. Registrar usuario', '07. Listar usuarios',
        '08. Libros por usuario', '09. Guardar datos', '10. Cargar datos', '00. Salir'
    ]

    draw_menu(stdscr, menu, current_row_idx)
    draw_content(stdscr, bienvenida)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            draw_menu(stdscr, menu, current_row_idx)
            if current_row_idx == 0:
                titulo = get_input(stdscr, "Título del libro: ")
                autor = get_input(stdscr, "Autor del libro: ")
                descripcion = get_input(stdscr, "Descripción del libro: ", max_length=200)
                cantidad = get_input(stdscr, "Cantidad de libros (por defecto 1): ")
                cantidad = int(cantidad) if cantidad.isdigit() else 1
                biblioteca.agregar_libro(titulo, autor, descripcion, cantidad)
                draw_content(stdscr, ["Libro agregado correctamente."])
            elif current_row_idx == 1:
                biblioteca.mostrar_libros(stdscr)
            elif current_row_idx == 2:
                titulo = get_input(stdscr, "Título del libro: ")
                biblioteca.mostrar_descripcion_libro(stdscr, titulo)
            elif current_row_idx == 3:
                titulo = get_input(stdscr, "Título del libro: ")
                nombre_usuario = get_input(stdscr, "Nombre del usuario: ")
                biblioteca.prestar_libro(stdscr, titulo, nombre_usuario)
            elif current_row_idx == 4:
                titulo = get_input(stdscr, "Título del libro: ")
                nombre_usuario = get_input(stdscr, "Nombre del usuario: ")
                biblioteca.devolver_libro(stdscr, titulo, nombre_usuario)
            elif current_row_idx == 5:
                nombre = get_input(stdscr, "Nombre del usuario: ")
                biblioteca.registrar_usuario(stdscr, nombre)
            elif current_row_idx == 6:
                biblioteca.listar_usuarios(stdscr)
            elif current_row_idx == 7:
                nombre_usuario = get_input(stdscr, "Nombre del usuario: ")
                biblioteca.listar_libros_usuario(stdscr, nombre_usuario)
            elif current_row_idx == 8:
                biblioteca.guardar_datos()
                draw_content(stdscr, ["Datos guardados correctamente."])
            elif current_row_idx == 9:
                biblioteca.cargar_datos()
                draw_content(stdscr, ["Datos cargados correctamente."])
            elif current_row_idx == 10:
                biblioteca.guardar_datos()
                draw_content(stdscr, ["Saliendo..."])
                break
        draw_menu(stdscr, menu, current_row_idx)

if __name__ == "__main__":
    curses.wrapper(main)
