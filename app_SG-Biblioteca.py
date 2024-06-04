import pickle
import os

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = 1

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor)

    def mostrar_libros(self):
        for titulo, libro in self.libros.items():
            disponibilidad = "Disponible" if libro.cantidad > 0 else "No disponible"
            print(f"Título: {titulo}, Autor: {libro.autor}, Cantidad: {libro.cantidad}, Disponibilidad: {disponibilidad}")

    def prestar_libro(self, titulo, nombre_usuario):
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
        if nombre in self.usuarios:
            print("Usuario ya registrado.")
        else:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado exitosamente.")

    def listar_usuarios(self):
        for nombre in self.usuarios:
            print(nombre)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            for libro in self.usuarios[nombre_usuario].libros_prestados:
                print(libro)
        else:
            print("Usuario no registrado.")

    def devolver_libro(self, titulo, nombre_usuario):
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
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)

    def cargar_datos(self):
        if os.path.exists('datos_biblioteca.pkl'):
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        else:
            self.libros = {}
            self.usuarios = {}

def mostrar_menu():
    print("\nMenú Biblioteca")
    print("LIBRO:   1. Agregar   | 2. Mostrar | 3. Prestar | 4. Devolver")
    print("USUARIO: 5. Registrar | 6. Listar  | 7. Libros x Usuarios")
    print("CONFIG.: 8. Guardar   | 9. Cargar  | 0. Salir")

def main():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            biblioteca.agregar_libro(titulo, autor)
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            titulo = input("Título del libro: ")
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.prestar_libro(titulo, nombre_usuario)
        elif opcion == "4":
            titulo = input("Título del libro: ")
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.devolver_libro(titulo, nombre_usuario)
        elif opcion == "5":
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)
        elif opcion == "6":
            biblioteca.listar_usuarios()
        elif opcion == "7":
            nombre_usuario = input("Nombre del usuario: ")
            biblioteca.listar_libros_usuario(nombre_usuario)
        elif opcion == "8":
            biblioteca.guardar_datos()
            print("Datos guardados correctamente.")
        elif opcion == "9":
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
