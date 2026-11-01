
from pathlib import Path

from pytest_bdd import scenarios, given, when, then, parsers

from screenplay.acciones import AbrirTienda
from screenplay.preguntas import ProductosDelCatalogo


FEATURE = Path(__file__).parent / "features" / "catalogo.feature"
scenarios(str(FEATURE))


@given("que el cliente abre la tienda")
def abrir_tienda(cliente, base_url_tienda):
    cliente.intenta(AbrirTienda(base_url_tienda))


@when("consulta el catálogo de productos")
def consultar_catalogo(cliente):
    assert cliente.page.get_by_test_id("vista-catalogo").is_visible()


@then("se muestran 24 productos")
def verificar_cantidad_productos(cliente):
    productos = ProductosDelCatalogo().consultar(cliente)
    assert productos.count() == 24, (
        f"Se esperaban 24 productos, pero aparecieron {productos.count()}"
    )


@then("cada producto presenta nombre, precio y categoría")
def verificar_datos_productos(cliente):
    productos = ProductosDelCatalogo().consultar(cliente)

    for i in range(productos.count()):
        producto = productos.nth(i)

        assert producto.get_by_test_id("nombre-producto").inner_text().strip()
        assert producto.get_by_test_id("precio-producto").inner_text().strip()
        assert producto.locator(".cat").inner_text().strip()
