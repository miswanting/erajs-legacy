import json
import os
import socket
import threading
import time
from . import EventManager
# from . import EventManager, LogManager

# import LogManager


class NetManager(EventManager.EventManager):
    HOST = 'localhost'
    PORT = 11994
    # _conn = None
    # _cmd_list = []
    _gui_list = []
    # isConnected = False

    def __init__(self) -> None:
        super().__init__()
        self.__connection = None
        self.__isConnected = False

    def connect(self):
        def core():
            while True:
                print()
                data = self.recv()
                for each in data:
                    # t = threading.Thread(target=self._parse_bag, args=(each,))
                    self._parse_bag(each)
                    # t.start()

        def func_connect():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
                self.__connection = c
                try:
                    self.__connection.connect((self.HOST, self.PORT))
                    self.__isConnected = True
                    self.info('│  └─ Connected!')
                    core()
                except OSError as err:
                    if err.errno == 10061:
                        self.warn('前端未启动！')
                        os._exit(1)
                    else:
                        self.error(err)
                        os._exit(1)

        t = threading.Thread(name='func_connect', target=func_connect)
        t.start()
        while True:
            if self.__isConnected:
                break
            time.sleep(0.1)
        # dispatcher.dispatch(event_type.SERVER_CONNECTED)

    def recv(self):
        data = self.__connection.recv(4096000)
        self.debug("接收：{}".format(data))
        if not data:
            return
        rawBags = data.decode().split('}{')
        for i in range(len(rawBags)):
            if not i == 0:
                rawBags[i] = '{' + rawBags[i]
            if not i == len(rawBags) - 1:
                rawBags[i] = rawBags[i] + '}'
        for i, each in enumerate(rawBags):
            rawBags[i] = json.loads(each)
        return rawBags

    def send(self, bag):
        self.debug("发送：{}".format(bag))
        self.__connection.send(json.dumps(bag, ensure_ascii=False).encode())

    def _parse_bag(self, bag: dict) -> None:
        target = ''
        value = {}
        if 'hash' in bag:
            target = bag['hash']
        if 'value' in bag:
            value = bag['value']
        self.emit(bag['type'], bag)

    def send_config(self):
        bag = {
            'type': 'init',
            'value': {
                'resolution': (800, 600)},
            'from': 'b',
            'to': 'm'
        }
        self.send(bag)
        # dispatcher.dispatch(event_type.SERVER_CONFIG_SENT)

    def send_loaded(self):
        bag = {
            'type': 'loaded',
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)

    def send_init_finished_signal(self):
        # logger.info('├─ Sending Loaded Signal to Server...')
        bag = {
            'type': 'loaded',
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)
        # dispatcher.dispatch(event_type.ENGINE_INIT_FINISHED_SIGNAL_SENT)
