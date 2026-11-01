
class ProductosDelCatalogo:
    def consultar(self, actor):
        return actor.page.get_by_test_id("grid-productos").locator(".card")


class ContadorDelCarrito:
    def consultar(self, actor):
        return int(
            actor.page.get_by_test_id("contador-carrito").inner_text()
        )


class PedidoConfirmado:
    def consultar(self, actor):
        mensaje = actor.page.get_by_test_id("mensaje-exito")
        return mensaje.is_visible()


class NumeroDePedido:
    def consultar(self, actor):
        return actor.page.get_by_test_id("numero-pedido").inner_text()
