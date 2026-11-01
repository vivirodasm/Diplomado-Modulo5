# Informe Final de Aseguramiento de Calidad
## Reto Práctico — Módulo 5: QA Cloud-Native

**Proyecto:** App Tienda  
**Repositorio:** vivirodasm/Diplomado-Modulo5  
**Rama:** reto-practico-modulo5  
**Fecha:** 1 de noviembre de 2026  
**Estado:** Implementación y validación de las fases 1 a 6, con publicación en ACR pendiente.

---

## 1. Introducción

El presente informe documenta las actividades de aseguramiento de calidad realizadas durante el Reto Práctico del Módulo 5, orientado a la implementación de estrategias de automatización, integración continua, pruebas en la nube y validación de contratos.

El proyecto utiliza una aplicación de comercio electrónico denominada **App Tienda**, desarrollada con Node.js y Express.

Durante el ejercicio se integraron herramientas como Faker, Azure DevOps, Playwright, pytest-bdd, Selenium, Sauce Labs, Podman y Pact.

## 2. Objetivo general

Implementar y validar una estrategia de automatización QA Cloud-Native que permita detectar defectos tempranamente, ejecutar pruebas en diferentes niveles y generar evidencias verificables de los resultados.

## 3. Fase 1 — Datos sintéticos

Se implementó la generación de datos de prueba mediante Faker.

**Resultados:**

- Generación de un catálogo de 24 productos.
- Distribución de productos en cuatro categorías.
- Datos utilizados para las pruebas funcionales y de API.

**Conclusión QA:** los datos sintéticos permiten disponer de información de prueba sin depender de registros reales de clientes.

## 4. Fase 2 — Integración continua con Azure DevOps

Se configuró un pipeline para automatizar las validaciones del proyecto.

**Etapas implementadas:**

- Build.
- SmokeTests.
- LoadTest.

Se incorporaron controles para detectar fallos durante las ejecuciones automatizadas.

**Resultado:** se obtuvieron ejecuciones exitosas del pipeline, registradas en Azure DevOps.

**Conclusión QA:** la integración continua permite ejecutar controles de calidad de forma repetible y detectar problemas antes de continuar con la entrega.

## 5. Fase 3 — BDD, Screenplay y Test Plans

Se implementaron escenarios de comportamiento mediante BDD y pruebas automatizadas con Playwright, pytest y pytest-bdd.

Se aplicó el patrón Screenplay para organizar la automatización.

**Resultados:**

- Cinco pruebas BDD/E2E aprobadas.
- Integración de pruebas automatizadas en Azure DevOps.
- Trabajo con Azure Test Plans para gestionar casos de prueba.

**Conclusión QA:** BDD facilita la descripción de comportamientos verificables y mejora la trazabilidad entre escenarios funcionales y automatización.

## 6. Fase 4 — Pruebas en la nube con Sauce Labs

Se integró Selenium con Sauce Labs para ejecutar pruebas remotas en un navegador Chrome sobre Windows 11.

Se utilizó Sauce Connect para permitir la comunicación con la aplicación durante la ejecución desde Azure DevOps.

**Resultados:**

- Se identificaron y corrigieron problemas de configuración del túnel.
- Las ejecuciones `#20261101.4` a `#20261101.8` registraron fallos.
- La ejecución `#20261101.9` finalizó exitosamente.
- Se confirmó una prueba aprobada en Sauce Labs.
- El pipeline completó cinco etapas exitosas.

**Conclusión QA:** la ejecución remota amplía las posibilidades de validación y permite integrar pruebas de navegador en un entorno de CI.

## 7. Fase 5 — Contenedores y Contract Testing

### 7.1. Contenerización

Se preparó un Dockerfile para ejecutar App Tienda en un contenedor mediante Podman.

**Validaciones realizadas:**

- Construcción exitosa de la imagen.
- Ejecución del contenedor.
- Estado saludable mediante HEALTHCHECK.
- Respuesta satisfactoria del endpoint `/api/health`.
- Consulta de 24 productos mediante `GET /api/productos`.

### 7.2. Pruebas de contrato Pact

Se implementaron pruebas de contrato utilizando Pact 17.1.4.

**Consumer Test:**

- Verificación de la estructura esperada de la respuesta del catálogo.
- Generación del contrato `TiendaFrontend-TiendaAPI.json`.
- Resultado: 1 prueba aprobada, 0 fallidas.

**Provider Verification:**

- Verificación del contrato contra la API real.
- Validación del endpoint `GET /api/productos`.
- Resultado: 1 prueba aprobada, 0 fallidas.

### 7.3. Arquitectura

Se documentó la comparación entre arquitectura monolítica y microservicios.

Para el alcance actual se recomienda mantener una arquitectura monolítica contenerizada, conservando la posibilidad de evolucionar hacia servicios independientes.

### 7.4. Actividad pendiente

La publicación de la imagen en Azure Container Registry (ACR) quedó pendiente debido a las condiciones de la suscripción y la necesidad de evitar costos no previstos.

**Conclusión QA:** la contenerización facilita la reproducibilidad del entorno y las pruebas Pact permiten detectar incompatibilidades entre consumidores y proveedores.

## 8. Fase 6 — Análisis de calidad

### 8.1. Métricas DORA

Se analizaron las cuatro métricas DORA:

- Deployment Frequency.
- Lead Time for Changes.
- Change Failure Rate.
- Time to Restore Service.

No se asignaron valores numéricos a estas métricas debido a la ausencia de registros suficientes de despliegues e incidentes en producción.

Como indicadores complementarios, se analizaron 11 ejecuciones del pipeline:

| Indicador | Resultado |
|---|---|
| Ejecuciones analizadas | 11 |
| Exitosas | 6 |
| Fallidas | 5 |
| Tasa de éxito de CI | 54,5 % |
| Tasa de fallo de CI | 45,5 % |

Estos porcentajes corresponden al pipeline y no deben confundirse con las métricas DORA de despliegue.

### 8.2. Pirámide de pruebas

Se identificaron los siguientes niveles:

- **Unitarias:** cobertura por fortalecer.
- **API e integración:** smoke tests, healthcheck y Pact.
- **E2E/UI:** Playwright, pytest-bdd, Selenium y Sauce Labs.

Se recomienda fortalecer las pruebas unitarias para reducir la dependencia de las pruebas E2E.

### 8.3. Análisis de riesgos

Se elaboró una matriz de riesgos que considera:

- Fallos de Sauce Connect.
- Incompatibilidades de API.
- Indisponibilidad de contenedores.
- Inestabilidad de pruebas E2E.
- Cobertura unitaria insuficiente.
- Costos de infraestructura.
- Vulnerabilidades en dependencias.
- Pérdida de evidencias.

Se documentaron acciones de mitigación y controles implementados.

## 9. Resultados generales

| Fase | Actividad principal | Resultado |
|---|---|---|
| 1 | Datos sintéticos con Faker | Completada |
| 2 | Pipeline de Azure DevOps | Completada |
| 3 | BDD, Screenplay y Test Plans | Completada |
| 4 | Sauce Labs y Selenium | Completada |
| 5 | Podman y Pact | Validaciones completadas; ACR pendiente |
| 6 | DORA, pirámide y riesgos | Análisis documentados |

## 10. Evidencias del proyecto

Las evidencias se encuentran organizadas en el directorio `RetoFinal/evidencias/`, por fase.

Entre las principales evidencias se incluyen:

- Resultados de pipelines en Azure DevOps.
- Ejecuciones BDD/E2E.
- Pruebas remotas de Sauce Labs.
- Construcción y ejecución del contenedor Podman.
- Respuesta de los endpoints de la aplicación.
- Pruebas Pact Consumer y Provider aprobadas.
- Publicación de cambios en GitHub.
- Historial de ejecuciones utilizado para el análisis DORA.

## 11. Recomendaciones de mejora

1. Fortalecer la cobertura de pruebas unitarias.
2. Mantener las pruebas de contrato ante cambios en la API.
3. Revisar las vulnerabilidades de dependencias reportadas durante la construcción del contenedor.
4. Implementar un registro de despliegues e incidentes para medir DORA.
5. Incorporar controles de estabilidad y disponibilidad de los entornos de prueba.
6. Evaluar la publicación en ACR cuando exista autorización y presupuesto.
7. Mantener las evidencias actualizadas y versionadas.

## 12. Conclusión técnica desde QA

El Reto Práctico del Módulo 5 permitió integrar diferentes herramientas y estrategias de automatización dentro de un flujo de aseguramiento de calidad Cloud-Native.

La combinación de pruebas funcionales, BDD, validaciones de API, ejecución remota, contenerización y pruebas de contrato permitió comprobar diferentes aspectos de la aplicación y detectar problemas de configuración durante la integración continua.

Los resultados obtenidos demuestran la importancia de automatizar los controles de calidad, mantener trazabilidad de las evidencias y validar los cambios antes de su entrega.

Como oportunidades de mejora permanecen el fortalecimiento de las pruebas unitarias, la revisión de dependencias y la implementación de mediciones DORA basadas en despliegues reales.

Desde QA, el principal aprendizaje es que la automatización no consiste únicamente en ejecutar pruebas, sino en construir un proceso reproducible, medible y sustentado en evidencias que contribuya a prevenir defectos y mejorar la confiabilidad del software.