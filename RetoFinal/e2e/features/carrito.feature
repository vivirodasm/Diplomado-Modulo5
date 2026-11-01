
# language: es
@carrito @TC18
Característica: Carrito de compras
  Como cliente de la tienda
  Quiero agregar productos al carrito
  Para realizar una compra

  Escenario: Agregar un producto al carrito
    Dado que el cliente abre la tienda
    Cuando agrega un producto al carrito
    Entonces el contador del carrito muestra 1 producto

  Escenario: Agregar dos productos al carrito
    Dado que el cliente abre la tienda
    Cuando agrega dos productos al carrito
    Entonces el contador del carrito muestra 2 productos
