import http.server
import os
import socketserver
import shutil

host = 'localhost'
port = 58373

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def copyfile(self, source, outputfile):
        try:
            shutil.copyfileobj(source, outputfile)
        except BrokenPipeError:
            print("BrokenPipeError: Client disconnected before response was fully sent.")

try:
    web_dir = '你的目录'
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