
import http from 'k6/http';
import { check } from 'k6';

const BASE_URL = __ENV.BASE_URL || 'http://localhost:3000';

export const options = {
  vus: 10,
  duration: '20s',
  thresholds: {
    http_req_duration: ['p(95)<800'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  const respuesta = http.get(`${BASE_URL}/api/productos`);

  check(respuesta, {
    'Catalogo responde HTTP 200': (r) => r.status === 200,
    'Catalogo devuelve productos': (r) => {
      try {
        return r.json().length === 24;
      } catch {
        return false;
      }
    },
  });
}
