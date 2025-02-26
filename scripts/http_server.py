from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"message": "Hello from the server!"}')

if __name__ == "__main__":
    webServer = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    print("Server started http://0.0.0.0:8080")
    webServer.serve_forever()