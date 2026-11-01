# Fase 6 — Análisis de métricas DORA

## 1. Objetivo

Evaluar el desempeño del proceso de desarrollo, integración continua y entrega de la aplicación **App Tienda**, utilizando como referencia las métricas DORA y los resultados obtenidos durante el Reto Práctico del Módulo 5.

## 2. Fuentes de información

Se utilizaron las siguientes fuentes:

- Historial de commits del repositorio Git.
- Historial de ejecuciones de Azure DevOps Pipelines.
- Resultados de pruebas automatizadas de las Fases 3 y 4.
- Evidencias de ejecución de pruebas en Sauce Labs.

**Período analizado:** 31 de octubre al 1 de noviembre de 2026.

## 3. Métricas DORA

### 3.1. Deployment Frequency — Frecuencia de despliegue

**Definición:** frecuencia con la que se realizan despliegues exitosos a un entorno objetivo, normalmente producción.

**Resultado:** no medido.

Se identificaron ejecuciones exitosas del pipeline de Azure DevOps, pero no se dispone de evidencia suficiente para confirmar despliegues a producción.

**Conclusión QA:** es necesario registrar los despliegues reales y sus fechas para calcular esta métrica.

### 3.2. Lead Time for Changes — Tiempo de entrega de cambios

**Definición:** tiempo transcurrido desde que un cambio se integra al código hasta que se despliega en producción.

**Resultado:** no medido.

Se analizaron 10 commits del repositorio, pero no se dispone de las fechas correspondientes a despliegues en producción.

**Conclusión QA:** los tiempos de ejecución del pipeline no deben confundirse con el tiempo de entrega de cambios.

### 3.3. Change Failure Rate — Tasa de fallos por cambio

**Definición:** proporción de despliegues que provocan fallos en el servicio y requieren intervención.

**Resultado:** no medido.

Durante la configuración de Sauce Labs se registraron cinco ejecuciones fallidas consecutivas del pipeline. Sin embargo, estos fallos ocurrieron durante la integración continua y no constituyen evidencia de incidentes posteriores a un despliegue.

**Conclusión QA:** se requiere relacionar los despliegues con los incidentes de servicio para calcular esta métrica.

### 3.4. Time to Restore Service — Tiempo de restauración del servicio

**Definición:** tiempo necesario para recuperar el servicio después de una interrupción.

**Resultado:** no medido.

No se dispone de registros de incidentes en producción con horas de inicio y recuperación.

**Conclusión QA:** se recomienda implementar un registro de incidentes que permita medir los tiempos de restauración.

## 4. Indicadores complementarios de integración continua

Aunque las métricas DORA no pueden calcularse completamente, Azure DevOps proporciona información útil sobre la estabilidad del pipeline.

### 4.1. Historial de ejecuciones

Se analizaron 11 ejecuciones del Reto Final:

| Indicador | Resultado |
|---|---|
| Total de ejecuciones analizadas | 11 |
| Ejecuciones exitosas | 6 |
| Ejecuciones fallidas | 5 |
| Tasa de éxito del pipeline | 54,5 % |
| Tasa de fallo del pipeline | 45,5 % |

Los resultados corresponden a las ejecuciones `#20261031.1` y `#20261101.1` hasta `#20261101.10`.

### 4.2. Análisis de fallos

Las ejecuciones `#20261101.4` a `#20261101.8` presentaron fallos durante la integración de Sauce Connect.

Posteriormente, las ejecuciones `#20261101.9` y `#20261101.10` finalizaron exitosamente con las cinco etapas del pipeline aprobadas.

Esto evidencia un proceso de identificación, corrección y validación de problemas de integración.

### 4.3. Actividad de desarrollo

El historial de Git muestra 10 commits entre el 31 de octubre y el 1 de noviembre de 2026.

Estos commits reflejan avances y correcciones incrementales, pero no representan necesariamente despliegues.

## 5. Interpretación desde QA

Los resultados muestran que la automatización permitió detectar problemas durante la integración de Sauce Labs antes de considerar la entrega final del proyecto.

Las ejecuciones fallidas facilitaron la identificación de dificultades de configuración y las ejecuciones posteriores confirmaron que los ajustes realizados permitieron completar el pipeline.

La existencia de pruebas funcionales, BDD, pruebas en la nube y pruebas de contrato fortalece el proceso de validación continua.

Sin embargo, para evaluar completamente el desempeño de entrega mediante DORA, es necesario complementar los registros de CI con información de despliegues e incidentes reales.

## 6. Recomendaciones

1. Registrar los despliegues exitosos a producción con fecha y versión.
2. Relacionar los commits con las versiones desplegadas.
3. Documentar los incidentes posteriores a los despliegues.
4. Registrar los tiempos de recuperación de los servicios.
5. Mantener los controles de calidad del pipeline antes de autorizar despliegues.
6. Monitorear periódicamente la tasa de éxito de las ejecuciones de CI.

## 7. Conclusión técnica

Desde la perspectiva de aseguramiento de calidad, el proyecto demuestra el valor de la integración continua y la automatización para detectar defectos y problemas de configuración tempranamente.

El análisis de 11 ejecuciones evidencia seis resultados exitosos y cinco fallidos, seguidos por una estabilización del pipeline.

Las cuatro métricas DORA quedan identificadas metodológicamente, pero no se asignan valores sin información suficiente sobre despliegues e incidentes.

Esta diferenciación permite presentar un análisis técnico sustentado en evidencias y evita confundir la estabilidad de CI con el desempeño operativo de producción.

## 8. Evidencias

- `evidencias/fase6/Fase6_Evidencia_Historial_Pipeline.png`
- `evidencias/fase6/Fase6_Evidencia_Pipeline_Fase4_Resultados.png`