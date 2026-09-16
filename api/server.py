import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from simulation.chem_model import metals_db


class MetalsRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metals":
            data = metals_db
        elif self.path.startswith("/metals/"):
            metal_name = self.path[len("/metals/"):]
            data = metals_db.get(metal_name)
            if data is None:
                self.send_response(404)
                self.end_headers()
                return
        else:
            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps(data).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


def start_server(host="127.0.0.1", port=8000):
    server = HTTPServer((host, port), MetalsRequestHandler)
    server.serve_forever()
