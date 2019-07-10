import http.server
import os
import threading
import webbrowser
from datetime import datetime

from . import LogManager

PORT = 81
DIR_PATH = 'erajs/front'


class FrontManager:
    def __init__(self):
        pass

    def init(self):
        pass

    def start_server(self):
        def start():
            handler = FrontServerHandler
            self.server = http.server.HTTPServer(("localhost", PORT), handler)
            print("serving at port", PORT)
            self.server.serve_forever()
        t = threading.Thread(target=start)
        t.start()

    def start_browser(self):
        webbrowser.open('http://localhost:81', 1)


class FrontServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        path = self.path
        if path == '/':
            path = 'index.html'
        file_path = '{}/{}'.format(DIR_PATH, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.wfile.write("{}: {}".format(self.command, path).encode())

    def log_message(self, format, *arg):
        date = datetime.today()
        print("[{}]({}){}".format(
            "SERV", date.strftime("%y%m%d-%H%M%S-%f"), ' '.join(arg)))
