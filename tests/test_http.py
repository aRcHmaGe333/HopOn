import json
from threading import Thread
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer

from hopon_app import Handler
from backend.service import HopOn

R = [[59.32, 18.05], [59.32, 18.06], [59.32, 18.075], [59.32, 18.09]]


def test_http_end_to_end():
    Handler.engine = HopOn()
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f'http://127.0.0.1:{server.server_port}'

    def req(path, body=None, token=None):
        data = None if body is None else json.dumps(body).encode()
        headers = {'Content-Type': 'application/json'}
        if token:
            headers['X-HopOn-Token'] = token
        with urlopen(Request(base + path, data=data, headers=headers), timeout=3) as response:
            return json.loads(response.read())

    try:
        assert req('/api/health')['status'] == 'ok'
        d = req('/api/drivers', {'route': R, 'position': R[0]})
        p = req('/api/rides', {'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
        assert p['status'] == 'assigned'
        assert len(req('/api/drivers/' + d['driver_id'] + '/rides', token=d['token'])['rides']) == 1
        req('/api/drivers/' + d['driver_id'], {'position': p['match']['pickup']}, d['token'])
        assert req('/api/rides/' + p['ride_id'], token=p['token'])['waiting_seconds'] is not None
        assert req('/api/rides/' + p['ride_id'] + '/action', {'action': 'board'}, p['token'])['status'] == 'boarded'
        assert req('/api/rides/' + p['ride_id'] + '/action', {'action': 'complete'}, d['token'])['status'] == 'completed'
        try:
            req('/api/rides/' + p['ride_id'], token='invalid')
            assert False, 'Unauthorized access succeeded'
        except HTTPError as e:
            assert e.code == 403
    finally:
        server.shutdown()
        server.server_close()
