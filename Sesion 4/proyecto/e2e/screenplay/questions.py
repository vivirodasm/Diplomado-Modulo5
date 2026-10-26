"""Questions: lo que el actor OBSERVA para verificar un resultado.

Cada Question sabe responderse "como" un actor y devuelve un valor
que el test compara con un assert.
"""
from .abilities import NavegarConElNavegador


def _page(actor):
    return actor.habilidad(NavegarConElNavegador).page


class ContadorCarrito:
    """Numero que muestra el contador del carrito en el header."""

    @staticmethod
    def valor() -> "ContadorCarrito":
        return ContadorCarrito()

    def responder_como(self, actor) -> int:
        texto = _page(actor).get_by_test_id("carrito-contador").inner_text()
        return int(texto.strip())


class ProductosVisibles:
    """Cantidad de tarjetas de producto visibles en el catalogo."""

    @staticmethod
    def cantidad() -> "ProductosVisibles":
        return ProductosVisibles()

    def responder_como(self, actor) -> int:
        return _page(actor).locator('[data-testid="lista-productos"] .card').count()


class CategoriasVisibles:
    """Lista de categorias (data-categoria) de las tarjetas visibles."""

    @staticmethod
    def lista() -> "CategoriasVisibles":
        return CategoriasVisibles()

    def responder_como(self, actor) -> list[str]:
        tarjetas = _page(actor).locator('[data-testid="producto-card"]')
        n = tarjetas.count()

        return [
            tarjetas.nth(i).locator(".categoria").inner_text().strip()
            for i in range(n)
        ]


class TotalDelCarrito:
    """Texto del total mostrado en el carrito (ej. 'Total: $123.00')."""

    @staticmethod
    def texto() -> "TotalDelCarrito":
        return TotalDelCarrito()

    def responder_como(self, actor) -> str:
        return _page(actor).get_by_test_id("carrito-total").inner_text()


class MensajeDeExitoVisible:
    """Verifica que aparezca el mensaje de pedido confirmado."""

    @staticmethod
    def estado() -> "MensajeDeExitoVisible":
        return MensajeDeExitoVisible()

    def responder_como(self, actor) -> bool:
        page = _page(actor)

        page.get_by_test_id("pedido-confirmado").wait_for(
            state="visible",
            timeout=15000
        )

        return page.get_by_test_id("pedido-confirmado").is_visible()