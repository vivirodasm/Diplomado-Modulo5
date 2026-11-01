
from pathlib import Path

from pytest_bdd import scenarios, given, when, then

from screenplay.acciones import (
    AbrirTienda,
    AgregarProducto,
    ConfirmarPedido,
)
from screenplay.preguntas import PedidoConfirmado, NumeroDePedido


FEATURE = Path(__file__).parent / "features" / "pedidos.feature"
scenarios(str(FEATURE))


@given("que el cliente abre la tienda")
def abrir_tienda(cliente, base_url_tienda):
    cliente.intenta(AbrirTienda(base_url_tienda))


@when("agrega un producto al carrito")
def agregar_producto(cliente):
    cliente.intenta(AgregarProducto(1))


@when("confirma el pedido con sus datos")
def confirmar_pedido(cliente):
    cliente.intenta(ConfirmarPedido("qa@test.com"))


@then("se muestra la confirmación del pedido")
def verificar_confirmacion(cliente):
    cliente.page.get_by_test_id("mensaje-exito").wait_for(
        state="visible"
    )
    assert PedidoConfirmado().consultar(cliente)


@then("el pedido queda registrado correctamente")
def verificar_pedido(cliente):
    numero = NumeroDePedido().consultar(cliente)
    assert numero.strip(), "El pedido no tiene número de confirmación"

    respuesta = cliente.page.request.get(
        "http://localhost:3000/api/pedidos"
    )
    assert respuesta.ok

    pedidos = respuesta.json()
    assert any(str(p["id"]) == numero for p in pedidos), (
        f"El pedido {numero} no aparece registrado en la API"
    )
