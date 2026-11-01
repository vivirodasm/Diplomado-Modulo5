
class AbrirTienda:
    def __init__(self, url):
        self.url = url

    def ejecutar(self, actor):
        actor.page.goto(self.url)
        actor.page.get_by_test_id("grid-productos").locator(".card").first.wait_for()


class AgregarProducto:
    def __init__(self, cantidad=1):
        self.cantidad = cantidad

    def ejecutar(self, actor):
        boton = actor.page.get_by_test_id("grid-productos").get_by_role(
            "button", name="Agregar al carrito"
        ).first

        for _ in range(self.cantidad):
            boton.click()


class ConfirmarPedido:
    def __init__(self, correo="qa@test.com"):
        self.correo = correo

    def ejecutar(self, actor):
        actor.page.get_by_test_id("abrir-carrito").click()
        actor.page.get_by_test_id("input-email").fill(self.correo)
        actor.page.get_by_test_id("confirmar-pedido").click()


class FiltrarPorCategoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def ejecutar(self, actor):
        actor.page.get_by_test_id("filtro-categoria").select_option(
            label=self.categoria
        )

