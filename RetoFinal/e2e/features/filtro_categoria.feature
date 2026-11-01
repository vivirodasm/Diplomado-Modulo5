
# language: es
@catalogo @claude_mcp
Característica: Filtro de catálogo por categoría
  Como cliente de la Tienda QA
  Quiero filtrar el catálogo por categoría
  Para ver únicamente los productos que me interesan

  Escenario: Al seleccionar la categoría "Hogar" solo se muestran productos de Hogar
    Dado que el usuario abre la tienda QA en el catálogo
    Cuando selecciona la categoría "Hogar" en el filtro
    Entonces solo se muestran productos de la categoría "Hogar"
