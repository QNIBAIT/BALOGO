import http.server
import os
import socketserver
import shutil

host = '0.0.0.0'
port = 40000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def copyfile(self, source, outputfile):
        try:
            shutil.copyfileobj(source, outputfile)
        except BrokenPipeError:
            print("BrokenPipeError: Client disconnected before response was fully sent.")

try:
    web_dir = 'Your Run file directory'
    os.chdir(web_dir)

    Handler = MyRequestHandler
    httpd = socketserver.TCPServer((host, port), Handler)
    httpd.timeout = 10

    print(f"Serving web files at http://{host}:{port}/")

    httpd.serve_forever()

except PermissionError:
    print("Permission denied: You don't have permission to access the specified directory.")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    if 'httpd' in locals():
        httpd.server_close()
        print("Server closed.")
        from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=40000)
