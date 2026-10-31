
import { faker } from '@faker-js/faker/locale/es';
import fs from 'node:fs';
import path from 'node:path';

faker.seed(2026);

const categorias = ['Tecnología', 'Hogar', 'Deportes', 'Ropa'];

const nombresPorCategoria = {
  'Tecnología': [
    'Teclado inalámbrico', 'Mouse óptico', 'Monitor LED',
    'Audífonos Bluetooth', 'Memoria USB', 'Cámara web'
  ],
  'Hogar': [
    'Licuadora', 'Cafetera', 'Juego de sábanas',
    'Lámpara de mesa', 'Aspiradora', 'Organizador'
  ],
  'Deportes': [
    'Balón de fútbol', 'Mancuernas', 'Colchoneta de yoga',
    'Bicicleta estática', 'Raqueta de tenis', 'Cuerda para saltar'
  ],
  'Ropa': [
    'Camiseta', 'Pantalón deportivo', 'Chaqueta',
    'Sudadera', 'Zapatos deportivos', 'Gorra'
  ]
};
const productos = [];

for (let i = 1; i <= 24; i++) {
  productos.push({
    id: i,
    nombre: nombresPorCategoria[categorias[(i - 1) % categorias.length]][Math.floor((i - 1) / categorias.length)],
    precio: Number(faker.commerce.price({ min: 10000, max: 500000 })),
    stock: faker.number.int({ min: 0, max: 100 }),
    categoria: categorias[(i - 1) % categorias.length]
  });
}

const archivo = path.join(import.meta.dirname, 'db.json');

fs.writeFileSync(
  archivo,
  JSON.stringify({ productos }, null, 2),
  'utf8'
);

console.log(`Catálogo generado: ${productos.length} productos`);
