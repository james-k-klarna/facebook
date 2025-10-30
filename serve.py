#!/usr/bin/env python3
"""
Simple HTTP server to serve the Jira landscape HTML file
This solves the CORS issue when loading local images
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Change to the directory containing the HTML file
os.chdir(Path(__file__).parent)

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local file access
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"Open http://localhost:{PORT}/jira-landscape.html in your browser")
        print("Press Ctrl+C to stop the server")
        
        # Try to open the browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}/jira-landscape.html')
        except:
            pass
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
