class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """
    def __init__(self, titulo, autor, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.cantidad = 1