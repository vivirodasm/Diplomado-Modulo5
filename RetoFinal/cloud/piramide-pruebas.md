# Fase 6 — Pirámide de pruebas automatizadas

## 1. Objetivo

Analizar los niveles de pruebas implementados en el proyecto **App Tienda**, identificar su contribución al aseguramiento de calidad y proponer mejoras para optimizar la estrategia de automatización.

## 2. Modelo de pirámide de pruebas

La pirámide de pruebas propone distribuir las verificaciones automatizadas en tres niveles principales:

| Nivel | Características | Objetivo |
|---|---|---|
| Pruebas unitarias | Rápidas, aisladas y de bajo costo | Validar funciones y reglas de negocio |
| Pruebas de API e integración | Verifican interfaces y comunicación entre componentes | Detectar defectos de integración |
| Pruebas E2E / UI | Ejecutan flujos completos desde la interfaz | Validar procesos funcionales desde la perspectiva del usuario |

Se recomienda mantener una base amplia de pruebas unitarias, complementada con pruebas de API y una cantidad selectiva de pruebas E2E.

## 3. Pruebas implementadas en App Tienda

### 3.1. Pruebas unitarias

No se ha confirmado una suite específica de pruebas unitarias en el alcance desarrollado del Reto Final.

**Estado:** oportunidad de mejora.

Se recomienda incorporar pruebas para las funciones de filtrado, cálculos del carrito, validación de cantidades y reglas de pedidos.

### 3.2. Pruebas de API e integración

Durante el proyecto se implementaron validaciones de API y pruebas de contrato.

**Tecnologías y validaciones:**

- Smoke tests de API en el pipeline de Azure DevOps.
- Verificación del endpoint `/api/health`.
- Consulta del catálogo mediante `GET /api/productos`.
- Pact Consumer Test para validar la estructura esperada de los productos.
- Pact Provider Verification contra la API real ejecutada en Podman.

**Resultado destacado:** las pruebas de contrato del consumidor y proveedor finalizaron con una prueba aprobada y cero fallidas en cada ejecución.

Estas pruebas permiten detectar incompatibilidades entre el consumidor y el proveedor antes de que afecten los flujos funcionales.

### 3.3. Pruebas E2E / UI

Se implementaron pruebas automatizadas para validar funcionalidades de la tienda desde la perspectiva del usuario.

**Tecnologías utilizadas:**

- Playwright.
- Py