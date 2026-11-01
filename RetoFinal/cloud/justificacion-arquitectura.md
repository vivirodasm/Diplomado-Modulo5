# Justificación técnica de arquitectura: Monolito vs. Microservicios

## 1. Contexto del proyecto

El proyecto **App Tienda**, desarrollado como parte del Reto Práctico del Módulo 5 — QA Cloud-Native, implementa una aplicación de comercio electrónico con funcionalidades de catálogo, carrito y pedidos.

La aplicación utiliza Node.js y Express, genera datos sintéticos mediante Faker y puede ejecutarse dentro de un contenedor utilizando Podman.

Se implementaron pruebas automatizadas y pruebas de contrato con Pact para validar la comunicación entre el consumidor (TiendaFrontend) y el proveedor (TiendaAPI).

## 2. Comparación de arquitecturas

| Criterio | Arquitectura monolítica | Arquitectura de microservicios |
|---|---|---|
| Despliegue | Una única aplicación | Servicios independientes |
| Complejidad | Menor complejidad operativa | Mayor complejidad de infraestructura |
| Escalabilidad | Escalamiento de la aplicación completa | Escalamiento independiente por servicio |
| Mantenimiento | Administración centralizada | Mantenimiento por componentes |
| Pruebas QA | Pruebas funcionales e integración directa | Requiere pruebas de integración y contratos entre servicios |
| Observabilidad | Monitoreo centralizado | Requiere monitoreo y trazabilidad distribuidos |

## 3. Justificación de la arquitectura seleccionada

Para el alcance actual de App Tienda se recomienda mantener una **arquitectura monolítica contenerizada**.

Esta decisión permite simplificar el despliegue, reducir la complejidad de infraestructura y facilitar la ejecución de pruebas automatizadas dentro de un pipeline de integración continua.

El uso de contenedores aporta portabilidad y reproducibilidad del entorno de ejecución, sin requerir que la aplicación se divida en múltiples servicios.

## 4. Importancia de Contract Testing

Se implementaron pruebas de contrato mediante Pact 17.1.4 para verificar el endpoint `GET /api/productos`.

Las validaciones realizadas fueron:

- **Consumer Test:** validación de la estructura esperada de la respuesta mediante un servidor simulado de Pact.
- **Provider Verification:** verificación del contrato contra la API real ejecutada en el contenedor.
- **Resultado:** ambas pruebas finalizaron exitosamente, con una prueba aprobada y cero fallidas en cada ejecución.

Estas pruebas permiten detectar incompatibilidades en los contratos de comunicación y resultan especialmente importantes en arquitecturas de microservicios, donde los consumidores y proveedores pueden evolucionar de forma independiente.

## 5. Posible evolución a microservicios

Si el proyecto aumenta su alcance, podrían separarse componentes como:

- Servicio de catálogo de productos.
- Servicio de carrito de compras.
- Servicio de pedidos.

Esta separación permitiría realizar despliegues y escalamiento independientes, aunque también requeriría fortalecer la observabilidad, la gestión de fallos de red y las pruebas de integración.

## 6. Conclusión técnica desde QA

La arquitectura monolítica contenerizada es adecuada para el alcance actual de App Tienda, porque permite mantener un entorno controlado, reproducible y sencillo de validar.

La implementación de Pact demuestra una estrategia de prevención de defectos de integración y establece una base para una posible evolución hacia microservicios.

Desde el enfoque de aseguramiento de calidad, la decisión arquitectónica debe considerar no solamente la escalabilidad, sino también la facilidad de prueba, la estabilidad de los despliegues y el costo de mantenimiento.