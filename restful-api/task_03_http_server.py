#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            new_dict = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(new_dict.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info_data = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(info_data.encode("utf-8"))

        
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, APIHandler)
    httpd.serve_forever()