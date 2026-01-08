import http.server
import socketserver

PORT = 8080

print("Chemistry Lab Pro - Server running")
print(f"Open: http://localhost:{PORT}")

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)
httpd.serve_forever()
