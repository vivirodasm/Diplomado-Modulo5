
const { PactV3, MatchersV3 } = require('@pact-foundation/pact');
const assert = require('node:assert/strict');
const path = require('node:path');
const { test } = require('node:test');

 const { integer, number, string, eachLike } = MatchersV3;

const pact = new PactV3({
  consumer: 'TiendaFrontend',
  provider: 'TiendaAPI',
  dir: path.resolve(__dirname, 'contracts'),
});

test('GET /api/productos devuelve el catalogo esperado', async () => {
  pact
    .given('existen productos en el catalogo')
    .uponReceiving('una solicitud para consultar productos')
    .withRequest({
      method: 'GET',
      path: '/api/productos',
    })
    .willRespondWith({
      status: 200,
      headers: {
        'Content-Type': 'application/json',
      },
      body: eachLike({
        id: integer(1),
        nombre: string('Tasty Concrete Chair'),
        categoria: string('hogar'),
        precio: number(106.25),
        descripcion: string('Descripcion del producto'),
        stock: integer(5),
      }),
    });

  await pact.executeTest(async (mockServer) => {
    const response = await fetch(
      `${mockServer.url}/api/productos`
    );

    assert.equal(response.status, 200);

    const productos = await response.json();

    assert.ok(Array.isArray(productos));
    assert.ok(productos.length > 0);

    for (const producto of productos) {
      assert.equal(typeof producto.id, 'number');
      assert.equal(typeof producto.nombre, 'string');
      assert.equal(typeof producto.categoria, 'string');
      assert.equal(typeof producto.precio, 'number');
      assert.equal(typeof producto.descripcion, 'string');
      assert.equal(typeof producto.stock, 'number');
    }

    console.log('PASSED: contrato consumer GET /api/productos');
  });
});
