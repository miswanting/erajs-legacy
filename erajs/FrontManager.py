import base64
import hashlib
import http.server
import os
import socketserver
import ssl
import threading
import webbrowser
from datetime import datetime

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from . import LogManager

HOST = 'localhost'
PORT = 81
DIR_PATH = 'erajs/front'
WS_MAGIC_STRING = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


class FrontManager:
    def __init__(self):
        pass

    def init(self):
        pass

    def start_server(self):
        def start():
            # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            # context.load_cert_chain(certfile="mycertfile")
            # handler = FrontServerHandler
            # self.server = socketserver.TCPServer((HOST, PORT), handler)
            # # self.server = http.server.HTTPServer(("localhost", PORT), handler)
            # print("serving at port", PORT)
            # self.server.serve_forever()
            server = SimpleWebSocketServer('', 8000, SimpleEcho)
            server.serveforever()

        t = threading.Thread(target=start)
        t.start()

    def start_browser(self):
        webbrowser.open('http://{}:{}'.format(HOST, PORT), 1)


class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


class FrontServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode()
        print('!', self.data)
        headers = self.data.split("\r\n")
        header = {}
        for line in headers:
            pair = line.split(': ')
            if len(pair) == 1:
                pair = line.split(' ')
                header['Method'] = pair[0]
                header['Path'] = pair[1]
                header['Version'] = pair[2]
            else:
                header[pair[0]] = pair[1]
        # WebSocket入口
        if "Connection: Upgrade" in self.data and "Upgrade: websocket" in self.data:
            for h in headers:
                if "Sec-WebSocket-Key" in h:
                    key = h.split(" ")[1]
            self.shake_hand(key)
            while True:
                payload = self.decode_frame(
                    bytearray(self.request.recv(1024).strip()))
                decoded_payload = payload.decode('utf-8')
                self.send_frame(payload)
                if "bye" == decoded_payload.lower():
                    "Bidding goodbye to our client..."
                    return
        else:  # HTTP入口
            path = header['Path']
            if path == '/':
                path = 'index.html'
            file_path = '{}/{}'.format(DIR_PATH, path)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf8') as f:
                    res = "HTTP/1.1 200\r\n" + \
                        "Content-Type: text/html\r\n" + \
                        "\r\n" + \
                        f.read()
                    self.request.sendall(res.encode())
            else:
                self.request.sendall("HTTP/1.1 400 Bad Request\r\n" +
                                     "Content-Type: text/plain\r\n" +
                                     "Connection: close\r\n" +
                                     "\r\n" +
                                     "Incorrect request")

    def shake_hand(self, key):
        # calculating response as per protocol RFC
        key = key + WS_MAGIC_STRING
        resp_key = base64.standard_b64encode(hashlib.sha1(key).digest())

        resp = "HTTP/1.1 101 Switching Protocols\r\n" + \
            "Upgrade: websocket\r\n" + \
            "Connection: Upgrade\r\n" + \
            "Sec-WebSocket-Accept: %s\r\n\r\n" % (resp_key)

        self.request.sendall(resp)

    def decode_frame(self, frame):
        opcode_and_fin = frame[0]

        # assuming it's masked, hence removing the mask bit(MSB) to get len. also assuming len is <125
        payload_len = frame[1] - 128

        mask = frame[2:6]
        encrypted_payload = frame[6: 6+payload_len]

        payload = bytearray([encrypted_payload[i] ^ mask[i % 4]
                             for i in range(payload_len)])

        return payload

    def send_frame(self, payload):
        # setting fin to 1 and opcpde to 0x1
        frame = [129]
        # adding len. no masking hence not doing +128
        frame += [len(payload)]
        # adding payload
        frame_to_send = bytearray(frame) + payload

        self.request.sendall(frame_to_send)

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
