"""HopOn local two-sided pilot server. Run: python hopon_app.py

No identity verification, real money, safe-road evaluation, or TLS.
Keep it on a trusted device or network only.
"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from backend.service import HopOn

BASE = Path(__file__).resolve().parent


class Handler(BaseHTTPRequestHandler):
    engine = HopOn()
    protocol_version = 'HTTP/1.1'

    def send_data(self, status, data, content_type='application/json; charset=utf-8'):
        data = data if isinstance(data, bytes) else json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.end_headers()
        self.wfile.write(data)

    def token(self):
        return self.headers.get('X-HopOn-Token', '')

    def body(self):
        try:
            n = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            raise ValueError('Invalid request length') from None
        if not 0 < n <= 16_384:
            raise ValueError('JSON request must be 1–16384 bytes')
        try:
            obj = json.loads(self.rfile.read(n).decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise ValueError('Invalid JSON') from None
        if not isinstance(obj, dict):
            raise ValueError('JSON object expected')
        return obj

    def handle_request(self, verb):
        parts = [p for p in urlsplit(self.path).path.split('/') if p]
        try:
            if verb == 'GET' and parts in ([], ['app']):
                return self.send_data(200, (BASE / 'web' / 'index.html').read_bytes(), 'text/html; charset=utf-8')
            if verb == 'GET' and parts == ['api', 'health']:
                return self.send_data(200, {'status': 'ok', 'mode': 'local-pilot'})
            if verb == 'POST' and parts == ['api', 'drivers']:
                return self.send_data(201, self.engine.register_driver(self.body()))
            if verb == 'POST' and len(parts) == 3 and parts[:2] == ['api', 'drivers']:
                return self.send_data(200, self.engine.update_driver(parts[2], self.token(), self.body()))
            if verb == 'GET' and len(parts) == 4 and parts[:2] == ['api', 'drivers'] and parts[3] == 'rides':
                return self.send_data(200, self.engine.driver_rides(parts[2], self.token()))
            if verb == 'POST' and parts == ['api', 'rides']:
                return self.send_data(201, self.engine.request_ride(self.body()))
            if len(parts) == 3 and parts[:2] == ['api', 'rides']:
                if verb == 'GET':
                    return self.send_data(200, self.engine.get_ride(parts[2], self.token()))
                if verb == 'POST':
                    return self.send_data(200, self.engine.update_passenger(parts[2], self.token(), self.body()))
            if verb == 'POST' and len(parts) == 4 and parts[:2] == ['api', 'rides'] and parts[3] == 'action':
                return self.send_data(200, self.engine.action(parts[2], self.token(), self.body().get('action')))
            self.send_data(404, {'error': 'Not found'})
        except PermissionError as e:
            self.send_data(403, {'error': str(e)})
        except (ValueError, TypeError, KeyError) as e:
            self.send_data(400, {'error': str(e)})

    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')


def main():
    parser = argparse.ArgumentParser(description='HopOn local pilot')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8787)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f'HopOn pilot: http://{args.host}:{server.server_port}  (Ctrl+C to exit)')
    if args.host not in ('localhost', '127.0.0.1', '::1'):
        print('DEMO ONLY: no TLS, identity verification or real payments; trusted network only')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
