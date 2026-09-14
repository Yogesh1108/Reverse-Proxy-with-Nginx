
from http.server import BaseHTTPRequestHandler, HTTPServer


class SparkFlowHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = f"""
SparkFlow Backend
=================

Request received successfully!

Path:
{self.path}

Method:
GET

Backend:
127.0.0.1:8080
"""

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())


server = HTTPServer(("127.0.0.1", 8081), SparkFlowHandler)

print("SparkFlow backend running on http://127.0.0.1:8080")

server.serve_forever()

