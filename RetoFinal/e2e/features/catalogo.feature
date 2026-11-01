
# language: es
@catalogo @TC17
Característica: Catálogo de productos
  Como cliente de la tienda
  Quiero consultar el catálogo
  Para conocer los productos disponibles

  Escenario: Visualizar los productos del catálogo
    Dado que el cliente abre la tienda
    Cuando consulta el catálogo de productos
    Entonces se muestran 24 productos
    Y cada producto presenta nombre, precio y categoría
