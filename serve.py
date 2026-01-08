import http.server
import socketserver
import os

PORT = 8080

print("Server starting on port", PORT)
print("Open: http://localhost:" + str(PORT))

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)
httpd.serve_forever()
