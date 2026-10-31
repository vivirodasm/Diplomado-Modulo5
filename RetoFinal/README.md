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