
# ============================================================
# Dockerfile - Reto Final Modulo 5
# Tienda QA - Frontend + API + Datos Faker
# Compatible con Docker y Podman
# ============================================================

# 1. Imagen base Node.js 20 Alpine
FROM node:20-alpine

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar archivos de dependencias
COPY package*.json ./

# 4. Copiar el generador de datos antes de npm install
# Necesario porque postinstall ejecuta generar-datos.js
COPY datos/generar-datos.js ./datos/generar-datos.js

# 5. Instalar dependencias de produccion
RUN npm install --omit=dev

# 6. Copiar frontend, servidor y demas archivos
COPY . .

# 7. Regenerar el catalogo con Faker
RUN node datos/generar-datos.js

# 8. Configurar puerto de la aplicacion
ENV PORT=3000

# 9. Exponer puerto HTTP
EXPOSE 3000

# 10. Healthcheck de la API
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:3000/api/health || exit 1

# 11. Iniciar servidor de Tienda QA
CMD ["node", "servidor/server.js"]
