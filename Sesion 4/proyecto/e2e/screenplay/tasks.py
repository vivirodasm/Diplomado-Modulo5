"""Tasks: acciones de negocio de alto nivel.

Cada Task se compone de interactions. Se leen como lo que hace un usuario:
    actor.intenta(AbrirElCatalogo())
    actor.intenta(FiltrarPorCategoria.llamada("hogar"))
    actor.intenta(AgregarProductoAlCarrito.con_id(1))
    actor.intenta(ConfirmarPedido.con_correo("ana@test.com"))
"""
from .interactions import Abrir, HacerClic, Escribir, Seleccionar
from .abilities import NavegarConElNavegador


class AbrirElCatalogo:
    def ejecutar_como(self, actor):
        actor.intenta(Abrir.la_pagina("/"))
        # Esperar a que el grid tenga al menos un producto
        page = actor.habilidad(NavegarConElNavegador).page
        page.wait_for_selector('[data-testid="lista-productos"] .card', timeout=10000)


class FiltrarPorCategoria:
    def __init__(self, categoria: str):
        self.categoria = categoria

    @staticmethod
    def llamada(categoria: str) -> "FiltrarPorCategoria":
        return FiltrarPorCategoria(categoria)

    def ejecutar_como(self, actor):
        actor.intenta(Seleccionar.el_valor(self.categoria).en("select-categoria"))


class AgregarProductoAlCarrito:
    def __init__(self, producto_id: int):
        self.producto_id = producto_id

    @staticmethod
    def con_id(producto_id: int) -> "AgregarProductoAlCarrito":
        return AgregarProductoAlCarrito(producto_id)

    def ejecutar_como(self, actor):
        page = actor.habilidad(NavegarConElNavegador).page

        # Abrir el detalle del producto por su ID
        actor.intenta(Abrir.la_pagina(f"/producto.html?id={self.producto_id}"))

        # Esperar a que aparezca el botón de agregar
        boton_agregar = page.get_by_test_id("btn-agregar")
        boton_agregar.wait_for(state="visible", timeout=15000)

        # Agregar el producto al carrito
        boton_agregar.click()

        # Confirmar que se agregó correctamente
        page.get_by_test_id("mensaje-agregado").wait_for(
            state="visible",
            timeout=10000
        )



class AbrirElCarrito:
    def ejecutar_como(self, actor):
        page = actor.habilidad(NavegarConElNavegador).page

        # Abrir el carrito desde la navegacion
        actor.intenta(HacerClic.en("nav-carrito"))

        # Esperar a que aparezca el contenido del carrito
        page.get_by_test_id("contenido-carrito").wait_for(
            state="visible",
            timeout=15000
        )

        # Verificar que el boton de confirmar este disponible
        page.get_by_test_id("btn-confirmar").wait_for(
            state="visible",
            timeout=15000
        )


class ConfirmarPedido:
    def __init__(self, correo: str):
        self.correo = correo

    @staticmethod
    def con_correo(correo: str) -> "ConfirmarPedido":
        return ConfirmarPedido(correo)

    def ejecutar_como(self, actor):
        page = actor.habilidad(NavegarConElNavegador).page

        # La tienda actual utiliza un correo fijo al confirmar
        # el pedido. No existe un campo input-email.
        actor.intenta(HacerClic.en("btn-confirmar"))

        # Esperar la confirmacion de la compra
        page.get_by_test_id("pedido-confirmado").wait_for(
            state="visible",
            timeout=15000
        )

