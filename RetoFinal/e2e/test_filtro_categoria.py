
from pathlib import Path

from pytest_bdd import scenarios, given, when, then

from screenplay.acciones import AbrirTienda, FiltrarPorCategoria
from screenplay.preguntas import ProductosDelCatalogo


FEATURE = Path(__file__).parent / "features" / "filtro_categoria.feature"
scenarios(str(FEATURE))


@given("que el usuario abre la tienda QA en el catálogo")
def abrir_catalogo(cliente, base_url_tienda):
    cliente.intenta(AbrirTienda(base_url_tienda))


@when('selecciona la categoría "Hogar" en el filtro')
def filtrar_hogar(cliente):
    cliente.intenta(FiltrarPorCategoria("Hogar"))


@then('solo se muestran productos de la categoría "Hogar"')
def verificar_productos_hogar(cliente):
    productos = ProductosDelCatalogo().consultar(cliente)

    assert productos.count() == 6, (
        f"Se esperaban 6 productos de Hogar, "
        f"pero aparecieron {productos.count()}"
    )

    for i in range(productos.count()):
        producto = productos.nth(i)
        assert producto.get_attribute("data-categoria") == "hogar"
