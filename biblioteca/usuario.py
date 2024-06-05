class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []