
class Actor:
    """Representa al usuario que realiza acciones en la tienda."""

    def __init__(self, nombre, page):
        self.nombre = nombre
        self.page = page

    def intenta(self, accion):
        """Ejecuta una acción utilizando Playwright."""
        return accion.ejecutar(self)
