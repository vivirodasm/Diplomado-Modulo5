# Fase 6 — Matriz de riesgos de QA

## 1. Objetivo

Identificar, evaluar y priorizar los riesgos técnicos y de calidad del proyecto **App Tienda**, desarrollado durante el Reto Práctico del Módulo 5 — QA Cloud-Native.

El propósito es establecer controles preventivos y acciones de mitigación que contribuyan a mejorar la estabilidad, seguridad y confiabilidad del proceso de automatización.

## 2. Metodología de evaluación

Los riesgos se evalúan utilizando dos criterios:

- **Probabilidad (P):** posibilidad de que ocurra el riesgo.
- **Impacto (I):** consecuencia sobre la calidad, disponibilidad o ejecución del proyecto.

Se utiliza una escala de 1 a 3:

| Valor | Probabilidad | Impacto |
|---|---|---|
| 1 | Baja | Bajo |
| 2 | Media | Medio |
| 3 | Alta | Alto |

**Nivel de riesgo = Probabilidad × Impacto**

| Puntuación | Clasificación |
|---|---|
| 1–2 | Bajo |
| 3–4 | Medio |
| 6–9 | Alto |

Las puntuaciones representan una evaluación cualitativa de QA, no frecuencias estadísticas medidas.

## 3. Matriz de riesgos

| ID | Riesgo | P | I | Nivel | Clasificación |
|---|---|---|---|---|---|
| R01 | Fallos de configuración en Sauce Connect | 3 | 3 | 9 | Alto |
| R02 | Cambios incompatibles en la API | 2 | 3 | 6 | Alto |
| R03 | Fallos de disponibilidad del contenedor | 2 | 3 | 6 | Alto |
| R04 | Inestabilidad de pruebas E2E | 2 | 2 | 4 | Medio |
| R05 | Cobertura insuficiente de pruebas unitarias | 3 | 2 | 6 | Alto |
| R06 | Costos no previstos en Azure | 2 | 2 | 4 | Medio |
| R07 | Vulnerabilidades en dependencias | 2 | 3 | 6 | Alto |
| R08 | Pérdida o ausencia de evidencias | 2 | 2 | 4 | Medio |

## 4. Análisis y mitigación

### R01 — Fallos de configuración en Sauce Connect

**Antecedente:** durante la Fase 4 se registraron cinco ejecuciones fallidas consecutivas del pipeline relacionadas con la integración de Sauce Connect.

**Impacto:** interrupción de las pruebas remotas y retraso en la validación del pipeline.

**Mitigación:** validar la instalación, configuración, disponibilidad y nombre del túnel antes de ejecutar las pruebas de Selenium en Sauce Labs.

**Evidencia:** ejecuciones fallidas `#20261101.4` a `#20261101.8` y posteriores ejecuciones exitosas.

### R02 — Cambios incompatibles en la API

**Antecedente:** la comunicación entre el consumidor y la API depende de una estructura de respuesta compatible.

**Impacto:** fallos en funcionalidades que consumen el catálogo.

**Mitigación:** mantener las pruebas de contrato Pact y ejecutarlas ante modificaciones de los endpoints.

**Control implementado:** Consumer Test y Provider Verification para `GET /api/productos`, ambas aprobadas.

### R03 — Fallos de disponibilidad del contenedor

**Antecedente:** la aplicación depende de la correcta ejecución del proceso Node.js dentro del contenedor.

**Impacto:** indisponibilidad de los endpoints de la tienda.

**Mitigación:** implementar healthcheck, validar el estado del contenedor y ejecutar smoke tests después de iniciarlo.

**Control implementado:** contenedor Podman saludable y endpoint `/api/health` con respuesta correcta.

### R04 — Inestabilidad de pruebas E2E

**Antecedente:** las pruebas de interfaz pueden verse afectadas por tiempos de carga, selectores y cambios visuales.

**Impacto:** falsos negativos, ejecuciones inconsistentes y mayor esfuerzo de mantenimiento.

**Mitigación:** utilizar selectores estables, esperas explícitas, trazas y evidencias de ejecución.

**Control implementado:** automatización con Playwright, pytest-bdd y Selenium en Sauce Labs.

### R05 — Cobertura insuficiente de pruebas unitarias

**Antecedente:** no se ha confirmado una suite completa de pruebas unitarias dentro del alcance del Reto Final.

**Impacto:** mayor dependencia de pruebas de integración y E2E para detectar defectos de lógica de negocio.

**Mitigación:** incorporar pruebas unitarias para filtrado, cálculos de carrito, validaciones y reglas de pedidos.

**Estado:** mejora pendiente.

### R06 — Costos no previstos en Azure

**Antecedente:** la publicación en Azure Container Registry quedó pendiente por consideraciones relacionadas con el estado de la suscripción y los posibles costos.

**Impacto:** consumo económico no previsto o imposibilidad de completar la publicación.

**Mitigación:** revisar los precios y las condiciones de la suscripción, establecer alertas de presupuesto y solicitar autorización antes de crear recursos facturables.

**Estado:** publicación ACR pendiente.

### R07 — Vulnerabilidades en dependencias

**Antecedente:** durante la construcción del contenedor, npm reportó advertencias de vulnerabilidades en dependencias de la aplicación.

**Impacto:** posible exposición a fallos de seguridad.

**Mitigación:** ejecutar `npm audit`, revisar los paquetes afectados y aplicar actualizaciones compatibles, verificando posteriormente las pruebas de regresión.

**Estado:** revisión de dependencias pendiente.

### R08 — Pérdida o ausencia de evidencias

**Antecedente:** el proyecto requiere evidencias verificables de las pruebas y ejecuciones realizadas.

**Impacto:** dificultad para demostrar resultados y trazabilidad de las validaciones.

**Mitigación:** organizar las capturas por fase, mantener nombres descriptivos y versionar los archivos relevantes en GitHub.

**Control implementado:** carpetas de evidencias y publicación de resultados de las Fases 4 y 5.

## 5. Priorización de acciones

Se recomienda atender primero los riesgos altos, especialmente los relacionados con disponibilidad, compatibilidad de API, seguridad de dependencias y cobertura de pruebas.

El riesgo R01 ya cuenta con una corrección validada mediante ejecuciones exitosas, aunque debe mantenerse el control preventivo para evitar recurrencias.

Los riesgos medios deben incluirse en el seguimiento del proyecto, particularmente la gestión de costos y la conservación de evidencias.

## 6. Conclusión técnica desde QA

El análisis identifica riesgos asociados con infraestructura, integración continua, automatización funcional, contratos de API, seguridad y trazabilidad.

Durante el proyecto se implementaron controles efectivos, como las pruebas de contrato Pact, los healthchecks de Podman y las validaciones remotas mediante Sauce Labs.

No obstante, permanecen oportunidades de mejora relacionadas con la cobertura unitaria, el análisis de dependencias y la publicación en Azure Container Registry.

La matriz permite priorizar acciones de prevención y mitigación, fortaleciendo la estrategia de aseguramiento de calidad y la estabilidad del proceso de entrega continua.

## 7. Evidencias relacionadas

- Historial de Azure DevOps Pipelines de la Fase 4.
- Ejecuciones exitosas de Sauce Labs.
- Evidencias del contenedor Podman y healthcheck.
- Resultados de Pact Consumer y Provider.
- Repositorio GitHub con los cambios y evidencias versionadas.