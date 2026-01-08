import http.server
import socketserver

PORT = 8081

print("Chemistry Lab Pro Server")
print("========================")
print(f"Server running on port {PORT}")
print(f"Open: http://localhost:{PORT}")
print("Press Ctrl+C to stop")

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
