# Reto Final — Módulo 5
## QA Cloud-Native: Automatización Inteligente con IA Generativa

Este proyecto desarrolla las seis fases del reto práctico final del Módulo 5, integrando automatización de pruebas, inteligencia artificial, CI/CD, contenedores y métricas de calidad.

## Fase 1 — Generación de datos de prueba

### Objetivo
Generar un catálogo reproducible para una aplicación de comercio electrónico utilizando Faker y una semilla fija.

### Implementación
- **Herramienta:** Faker para JavaScript.
- **Semilla fija:** `2026`.
- **Cantidad:** 24 productos.
- **Categorías:** Tecnología, Hogar, Deportes y Ropa.
- **Distribución:** 6 productos por categoría.
- **Campos:** `id`, `nombre`, `precio`, `stock` y `categoria`.

### Ejecución

Desde la carpeta `RetoFinal`:

```bash
npm install
node datos/generar-datos.js
```

El script genera automáticamente el archivo `datos/db.json`.

### Reproducibilidad

Se ejecutó el generador dos veces y se comparó el hash SHA256 del archivo resultante.

Ambas ejecuciones produjeron el mismo hash:

`B2439935F1F7217C8BC7E8E11D2BCF60FD45A571076F928428ADB49EC74BE8C0`

Esto demuestra que, con el código y las dependencias utilizadas, se obtiene el mismo catálogo.

### Estrategia de versionamiento

El archivo `db.json` no se versiona en Git porque contiene datos generados que pueden reconstruirse automáticamente mediante el script y la semilla fija.

Esto evita almacenar archivos derivados innecesarios y facilita la regeneración del catálogo durante la ejecución del pipeline.

**Entrega:** el archivo `db.json` se adjuntará por separado como evidencia del resultado generado.

### Evidencias

- `evidencias/fase1/Fase1_Reproducibilidad.png`
- Archivo `datos/db.json` generado.

### Estado

Fase 1: generación y reproducibilidad verificadas. Pendiente integrar la regeneración de datos al pipeline de CI/CD.

## Fase 2 — Integración continua y Quality Gates

### Objetivo
Implementar un pipeline en Azure DevOps que automatice la construcción de la aplicación y la ejecución de controles de calidad.

### Implementación
- **Plataforma:** Azure DevOps Pipelines.
- **Aplicación:** Node.js y Express.
- **Etapas iniciales:** Build, SmokeTests y LoadTest.
- **Quality Gates:** validaciones para permitir o detener el proceso según los resultados.

### Resultados
Se configuró y ejecutó el pipeline, comprobando tanto escenarios exitosos como situaciones de fallo.

### Evidencias
- `evidencias/fase2/Fase2_AzurePipeline.png`
- `evidencias/fase2/Fase2_QualityGate_GREEN.png`
- `evidencias/fase2/Fase2_QualityGate_RED.png`

### Estado
**Completada.** Pipeline y controles de calidad implementados.

---

## Fase 3 — BDD, Screenplay y Azure Test Plans

### Objetivo
Implementar automatización funcional basada en comportamientos y relacionarla con casos de prueba.

### Implementación
- **Herramientas:** Playwright, pytest y pytest-bdd.
- **Patrón de automatización:** Screenplay.
- **Gestión de pruebas:** Azure Test Plans.
- **IA generativa:** uso de Claude y Playwright MCP durante el desarrollo de escenarios.

### Resultados
- Cinco pruebas BDD/E2E aprobadas.
- Ejecución de pruebas dentro del pipeline.
- Gestión y asociación de casos en Azure Test Plans.

### Evidencias
- `evidencias/fase3/Fase3_Azure_JUnit_5_Passed.png`
- `evidencias/fase3/Fase3_AzureTestPlans.png`
- `evidencias/fase3/Fase3_TestPlans_Asociaciones.png`
- `evidencias/fase3/Fase3_Claude_Playwright_MCP.png`

### Estado
**Completada.** Automatización BDD y validaciones integradas.

---

## Fase 4 — Pruebas en la nube con Sauce Labs

### Objetivo
Ejecutar pruebas automatizadas en infraestructura de navegador remota e integrarlas al pipeline de Azure DevOps.

### Implementación
- **Herramientas:** Selenium y Sauce Labs.
- **Navegador:** Chrome sobre Windows 11.
- **Conectividad:** Sauce Connect.
- **Integración:** ejecución desde Azure DevOps.

### Resultados
Durante la integración se identificaron problemas de configuración y disponibilidad del túnel Sauce Connect.

Después de aplicar las correcciones, las ejecuciones `#20261101.9` y `#20261101.10` finalizaron exitosamente.

Se confirmó una prueba aprobada en Sauce Labs y la ejecución satisfactoria de las cinco etapas del pipeline.

### Evidencias
- `evidencias/fase4/Fase4_Evidencia_Pipeline_Azure_5_Etapas_Passed.png`
- `evidencias/fase4/Fase4_Evidencia_SauceLabs_Test_Passed.png`
- `evidencias/fase4/fase4_sauce_connect_activo.png`

### Estado
**Completada.** Pruebas remotas integradas y validadas.

---

## Fase 5 — Contenedores, arquitectura y Pact

### Objetivo
Contenerizar la aplicación, validar su disponibilidad e implementar pruebas de contrato entre consumidor y proveedor.

### Implementación

**Contenerización**
- Podman para construcción y ejecución de la imagen.
- Dockerfile de la aplicación.
- HEALTHCHECK para verificar disponibilidad.

**Pruebas de contrato**
- Pact 17.1.4.
- Consumer Test.
- Provider Verification.
- Contrato generado: `contracts/TiendaFrontend-TiendaAPI.json`.

**Arquitectura**
- Comparación entre monolito y microservicios.
- Justificación documentada en `cloud/justificacion-arquitectura.md`.

### Resultados
- Imagen construida exitosamente.
- Contenedor ejecutado con estado saludable.
- Endpoint `/api/health` validado.
- Endpoint `/api/productos` con 24 productos.
- Pact Consumer: 1 prueba aprobada.
- Pact Provider: 1 prueba aprobada.

### Evidencias
- `evidencias/fase5/Fase5_Evidencia_Podman_Build.png`
- `evidencias/fase5/Fase5_Evidencia_Contenedor_Healthy.png`
- `evidencias/fase5/Fase5_Evidencia_Pact_Consumer_Passed.png`
- `evidencias/fase5/Fase5_Evidencia_Pact_Provider_Passed.png`
- `evidencias/fase5/Fase5_Evidencia_Pact_Contrato_Generado.png`

### Actividad pendiente
La publicación de la imagen en Azure Container Registry (ACR) no se realizó debido a las condiciones de la suscripción de Azure y la necesidad de evitar costos no previstos.

### Estado
**Validaciones locales y contract testing completados. ACR pendiente.**

---

## Fase 6 — Métricas DORA, pirámide de pruebas y análisis de riesgos

### Objetivo
Evaluar los resultados de automatización y establecer oportunidades de mejora desde el aseguramiento de calidad.

### Métricas DORA
Se documentaron las cuatro métricas DORA y se analizaron los resultados disponibles del pipeline.

| Indicador de CI | Resultado |
|---|---|
| Ejecuciones analizadas | 11 |
| Ejecuciones exitosas | 6 |
| Ejecuciones fallidas | 5 |
| Tasa de éxito | 54,5 % |
| Tasa de fallo | 45,5 % |

Los resultados anteriores corresponden a ejecuciones de CI y no representan métricas DORA de despliegues en producción.

### Pirámide de pruebas
Se analizaron tres niveles:

- Pruebas unitarias: cobertura por fortalecer.
- Pruebas de API e integración: smoke tests, healthcheck y Pact.
- Pruebas E2E/UI: Playwright, BDD, Selenium y Sauce Labs.

### Matriz de riesgos
Se identificaron riesgos asociados con infraestructura, contratos de API, estabilidad de pruebas, seguridad de dependencias, cobertura y costos.

### Documentación
- `cloud/metricas-dora.md`
- `cloud/piramide-pruebas.md`
- `cloud/matriz-riesgos.md`

### Evidencias
- `evidencias/fase6/Fase6_Evidencia_Historial_Pipeline.png`
- `evidencias/fase6/Fase6_Evidencia_Pipeline_Fase4_Resultados.png`

### Estado
**Completada.** Análisis técnicos documentados.

---

## Informe final de QA

Se preparó un informe técnico que reúne los objetivos, implementaciones, resultados, evidencias y conclusiones de las seis fases.

**Documento:** `informe-final/Informe_Final_QA_Modulo5_Con_Evidencias.docx`

## Repositorio

**GitHub:** https://github.com/vivirodasm/Diplomado-Modulo5

**Rama de trabajo:** `reto-practico-modulo5`

## Conclusión general

El Reto Final del Módulo 5 permitió integrar datos sintéticos, integración continua, automatización BDD, pruebas remotas, contenedores y contract testing dentro de una estrategia QA Cloud-Native.

Las ejecuciones y evidencias obtenidas permiten demostrar controles de calidad automatizados y establecer oportunidades de mejora relacionadas con pruebas unitarias, seguridad y métricas de entrega.

La publicación en Azure Container Registry permanece pendiente.