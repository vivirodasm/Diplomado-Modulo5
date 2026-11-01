
const { Verifier } = require('@pact-foundation/pact');
const path = require('node:path');
const { test } = require('node:test');

const pactFile = path.resolve(
  __dirname,
  'contracts',
  'TiendaFrontend-TiendaAPI.json'
);

test('Provider: verificar contrato GET /api/productos', async () => {
  const verifier = new Verifier({
    provider: 'TiendaAPI',
    providerBaseUrl: 'http://localhost:3001',
    pactUrls: [pactFile],

    stateHandlers: {
      'existen productos en el catalogo': async () => {
        console.log('Estado confirmado: catalogo disponible');
      },
    },

    providerVersion: '1.0.0',
    publishVerificationResult: false,
  });

  await verifier.verifyProvider();

  console.log('PASSED: API real cumple el contrato Pact');
});
