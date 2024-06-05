import pickle
import os
from .libro import Libro
from .usuario import Usuario

class Biblioteca:
    """
    Clase que maneja la lógica de la biblioteca, incluyendo gestión de libros y usuarios.
    """
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor, descripcion):
        """
        Agrega un libro a la biblioteca. Si el libro ya existe, incrementa su cantidad.
        """
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor, descripcion)

    def mostrar_libros(self):
        """
        Muestra todos los libros disponibles en la biblioteca con su cantidad y estado.
        """
        for titulo, libro in self.libros.items():
            disponibilidad = "Disponible" if libro.cantidad > 0 else "No disponible"
            print(f"Cant: {libro.cantidad} - Título: {titulo}, Autor: {libro.autor}, Estado: {disponibilidad}")

    def mostrar_descripcion_libro(self, titulo):
        """
        Muestra la descripción de un libro específico.
        """
        if titulo in self.libros:
            libro = self.libros[titulo]
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Descripción: {libro.descripcion}, Cantidad: {libro.cantidad}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def prestar_libro(self, titulo, nombre_usuario):
        """
        Presta un libro a un usuario registrado, si el libro está disponible.
        """
        if nombre_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if titulo not in self.libros or self.libros[titulo].cantidad == 0:
            print("Libro no disponible.")
            return
        self.libros[titulo].cantidad -= 1
        self.usuarios[nombre_usuario].libros_prestados.append(titulo)
        print(f"Libro '{titulo}' prestado a {nombre_usuario}.")

    def registrar_usuario(self, nombre):
        """
        Registra un nuevo usuario en la biblioteca.
        """
        if nombre in self.usuarios:
            print("Usuario ya registrado.")
        else:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado exitosamente.")

    def listar_usuarios(self):
        """
        Lista todos los usuarios registrados en la biblioteca.
        """
        for nombre in self.usuarios:
            print(nombre)

    def listar_libros_usuario(self, nombre_usuario):
        """
        Lista los libros prestados a un usuario específico.
        """
        if nombre_usuario in self.usuarios:
            for libro in self.usuarios[nombre_usuario].libros_prestados:
                print(libro)
        else:
            print("Usuario no registrado.")

    def devolver_libro(self, titulo, nombre_usuario):
        """
        Permite a un usuario devolver un libro prestado.
        """
        if nombre_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if titulo not in self.usuarios[nombre_usuario].libros_prestados:
            print("El usuario no tiene este libro prestado.")
            return
        self.usuarios[nombre_usuario].libros_prestados.remove(titulo)
        self.libros[titulo].cantidad += 1
        print(f"Libro '{titulo}' devuelto por {nombre_usuario}.")

    def guardar_datos(self):
        """
        Guarda los datos de la biblioteca en un archivo utilizando pickle.
        """
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)

    def cargar_datos(self):
        """
        Carga los datos de la biblioteca desde un archivo utilizando pickle.
        """
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        else:
            self.libros = {}
            self.usuarios = {}
