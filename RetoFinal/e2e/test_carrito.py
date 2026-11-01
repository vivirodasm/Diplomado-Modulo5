
from pathlib import Path

from pytest_bdd import scenarios, given, when, then

from screenplay.acciones import AbrirTienda, AgregarProducto
from screenplay.preguntas import ContadorDelCarrito


FEATURE = Path(__file__).parent / "features" / "carrito.feature"
scenarios(str(FEATURE))


@given("que el cliente abre la tienda")
def abrir_tienda(cliente, base_url_tienda):
    cliente.intenta(AbrirTienda(base_url_tienda))


@when("agrega un producto al carrito")
def agregar_un_producto(cliente):
    cliente.intenta(AgregarProducto(1))


@when("agrega dos productos al carrito")
def agregar_dos_productos(cliente):
    cliente.intenta(AgregarProducto(2))


@then("el contador del carrito muestra 1 producto")
def verificar_un_producto(cliente):
    assert ContadorDelCarrito().consultar(cliente) == 1


@then("el contador del carrito muestra 2 productos")
def verificar_dos_productos(cliente):
    assert ContadorDelCarrito().consultar(cliente) == 2
