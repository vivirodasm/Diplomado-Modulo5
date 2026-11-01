
# language: es
@pedidos @TC19
Característica: Creación de pedidos
  Como cliente de la tienda
  Quiero confirmar mis compras
  Para registrar un pedido correctamente

  Escenario: Crear un pedido con un producto
    Dado que el cliente abre la tienda
    Cuando agrega un producto al carrito
    Y confirma el pedido con sus datos
    Entonces se muestra la confirmación del pedido
    Y el pedido queda registrado correctamente
