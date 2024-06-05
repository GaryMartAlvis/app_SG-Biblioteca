import curses
from biblioteca.biblioteca import Biblioteca

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.clear()

    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    current_row_idx = 0
    menu = [
        '1. Agregar libro', '2. Mostrar libros', '3. Mostrar descripción', '4. Prestar libro',
        '5. Devolver libro', '6. Registrar usuario', '7. Listar usuarios',
        '8. Libros por usuario', '9. Guardar datos', '10. Cargar datos', '0. Salir'
    ]

    bienvenida = [
        "Bienvenido a la Biblioteca!",
        "Seleccione una opción del menú para empezar."
    ]

    def draw_menu():
        h, w = stdscr.getmaxyx()
        menu_width = int(w * 0.2)
        for idx, row in enumerate(menu):
            x = 0
            y = idx
            if idx == current_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row[:menu_width])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row[:menu_width])
        stdscr.refresh()

    def draw_content(content):
        h, w = stdscr.getmaxyx()
        content_x = int(w * 0.2) + 1
        for idx, row in enumerate(content):
            stdscr.addstr(idx, content_x, row[:w - content_x - 1])
        stdscr.refresh()

    def get_input(prompt):
        h, w = stdscr.getmaxyx()
        content_x = int(w * 0.2) + 1
        stdscr.addstr(0, content_x, prompt)
        stdscr.refresh()
        curses.echo()
        user_input = stdscr.getstr(1, content_x, 40).decode("utf-8")
        curses.noecho()
        stdscr.clear()
        return user_input

    draw_menu()
    draw_content(bienvenida)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            draw_menu()
            if current_row_idx == 0:
                titulo = get_input("Título del libro: ")
                autor = get_input("Autor del libro: ")
                descripcion = get_input("Descripción del libro: ")
                biblioteca.agregar_libro(titulo, autor, descripcion)
                draw_content(["Libro agregado correctamente."])
            elif current_row_idx == 1:
                biblioteca.mostrar_libros(stdscr)
            elif current_row_idx == 2:
                titulo = get_input("Título del libro: ")
                biblioteca.mostrar_descripcion_libro(stdscr, titulo)
            elif current_row_idx == 3:
                titulo = get_input("Título del libro: ")
                nombre_usuario = get_input("Nombre del usuario: ")
                biblioteca.prestar_libro(stdscr, titulo, nombre_usuario)
            elif current_row_idx == 4:
                titulo = get_input("Título del libro: ")
                nombre_usuario = get_input("Nombre del usuario: ")
                biblioteca.devolver_libro(stdscr, titulo, nombre_usuario)
            elif current_row_idx == 5:
                nombre = get_input("Nombre del usuario: ")
                biblioteca.registrar_usuario(stdscr, nombre)
            elif current_row_idx == 6:
                biblioteca.listar_usuarios(stdscr)
            elif current_row_idx == 7:
                nombre_usuario = get_input("Nombre del usuario: ")
                biblioteca.listar_libros_usuario(stdscr, nombre_usuario)
            elif current_row_idx == 8:
                biblioteca.guardar_datos()
                draw_content(["Datos guardados correctamente."])
            elif current_row_idx == 9:
                biblioteca.cargar_datos()
                draw_content(["Datos cargados correctamente."])
            elif current_row_idx == 10:
                biblioteca.guardar_datos()
                draw_content(["Saliendo..."])
                break
        draw_menu()

if __name__ == "__main__":
    curses.wrapper(main)
