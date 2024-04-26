import http.server
import socketserver

# Define the directory containing static files
STATIC_DIR = "static"

# Define the port on which to run the server
PORT = 8000

# Define the request handler class
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the do_GET method to customize request handling
    def do_GET(self):
        # Set the directory for serving static files
        self.directory = STATIC_DIR
        # Call the parent class method to handle the request
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create a TCP server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Server running at port", PORT)
    # Start the server and keep it running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
