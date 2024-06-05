import pickle
import os
from .libro import Libro
from .usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor, descripcion):
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor, descripcion)

    def mostrar_libros(self, stdscr):
        content = []
        for titulo, libro in self.libros.items():
            disponibilidad = "Disponible" if libro.cantidad > 0 else "No disponible"
            content.append(f"Cant: {libro.cantidad} - Título: {titulo}, Autor: {libro.autor}, Estado: {disponibilidad}")
        self._draw_content(stdscr, content)

    def mostrar_descripcion_libro(self, stdscr, titulo):
        if titulo in self.libros:
            libro = self.libros[titulo]
            content = [f"Título: {libro.titulo}", f"Autor: {libro.autor}", f"Descripción: {libro.descripcion}", f"Cantidad: {libro.cantidad}"]
        else:
            content = ["El libro no se encuentra en la biblioteca."]
        self._draw_content(stdscr, content)

    def prestar_libro(self, stdscr, titulo, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            content = ["Usuario no registrado."]
        elif titulo not in self.libros or self.libros[titulo].cantidad == 0:
            content = ["Libro no disponible."]
        else:
            self.libros[titulo].cantidad -= 1
            self.usuarios[nombre_usuario].libros_prestados.append(titulo)
            content = [f"Libro '{titulo}' prestado a {nombre_usuario}."]
        self._draw_content(stdscr, content)

    def devolver_libro(self, stdscr, titulo, nombre_usuario):
        if nombre_usuario not in self.usuarios:
            content = ["Usuario no registrado."]
        elif titulo not in self.usuarios[nombre_usuario].libros_prestados:
            content = ["El usuario no tiene este libro prestado."]
        else:
            self.usuarios[nombre_usuario].libros_prestados.remove(titulo)
            self.libros[titulo].cantidad += 1
            content = [f"Libro '{titulo}' devuelto por {nombre_usuario}."]
        self._draw_content(stdscr, content)

    def registrar_usuario(self, stdscr, nombre):
        if nombre in self.usuarios:
            content = ["Usuario ya registrado."]
        else:
            self.usuarios[nombre] = Usuario(nombre)
            content = [f"Usuario '{nombre}' registrado exitosamente."]
        self._draw_content(stdscr, content)

    def listar_usuarios(self, stdscr):
        content = [nombre for nombre in self.usuarios]
        self._draw_content(stdscr, content)

    def listar_libros_usuario(self, stdscr, nombre_usuario):
        if nombre_usuario in self.usuarios:
            content = [libro for libro in self.usuarios[nombre_usuario].libros_prestados]
        else:
            content = ["Usuario no registrado."]
        self._draw_content(stdscr, content)

    def guardar_datos(self):
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)

    def cargar_datos(self):
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        else:
            self.libros = {}
            self.usuarios = {}

    def _draw_content(self, stdscr, content):
        h, w = stdscr.getmaxyx()
        content_x = int(w * 0.2) + 1
        stdscr.addstr(0, content_x, '-' * (w - content_x - 1))
        for idx, row in enumerate(content):
            stdscr.addstr(idx + 1, content_x, row[:w - content_x - 1])
        stdscr.refresh()
