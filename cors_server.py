import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow all origins
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Custom-Header')
        super().end_headers()

PORT = 8000

handler = CORSRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
