
import assert from 'node:assert/strict';

const BASE_URL = process.env.BASE_URL || 'http://localhost:3000';

async function ejecutarPruebas() {
  // 1. Health Check
  const health = await fetch(`${BASE_URL}/api/health`);
  assert.equal(health.status, 200);
  const salud = await health.json();
  assert.equal(salud.estado, 'ok');
  console.log('PASS - Health Check');

  // 2. Catalogo
  const catalogo = await fetch(`${BASE_URL}/api/productos`);
  assert.equal(catalogo.status, 200);
  const productos = await catalogo.json();
  assert.equal(productos.length, 24);
  console.log('PASS - Catalogo: 24 productos');

  // 3. Crear pedido
  const respuesta = await fetch(`${BASE_URL}/api/pedidos`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      productoId: productos[0].id,
      cliente: 'Cliente QA Smoke',
      cantidad: 1
    })
  });

  assert.equal(respuesta.status, 201);
  const pedido = await respuesta.json();
  assert.equal(pedido.estado, 'pendiente');
  assert.equal(pedido.productoId, productos[0].id);
  assert.ok(pedido.total > 0);
  console.log('PASS - Creacion de pedido');

  console.log('\nSMOKE TESTS: 3/3 PASSED');
}

ejecutarPruebas().catch((error) => {
  console.error('SMOKE TESTS FAILED:', error.message);
  process.exit(1);
});
