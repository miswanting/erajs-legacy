# coding:utf-8
import os
import csv
import sys
import glob
import time
import json
import random
import socket
import hashlib
# import graphene
import importlib
import threading
import configparser


def new_hash():
    m = hashlib.md5()
    m.update(str(random.random()).encode("utf-8"))
    return m.hexdigest().upper()


class DataEngine:
    data = {}
    pool = []

    def fix_path(self):
        if getattr(sys, 'frozen', False):
            # frozen
            d = os.path.dirname(sys.executable)
            gamepath = os.path.dirname(d)
        else:
            # unfrozen
            d = os.path.dirname(os.path.realpath(__file__))
            gamepath = os.path.dirname(os.path.dirname(d))
        sys.path.append(gamepath)

    def self_check(self):
        check_folder_list = [
            'config',
            'erajs/plugin',
            'erajs/prototype',
            'game',
            'dlc',
            'mod',
            'data',
            'save'
        ]
        for each in check_folder_list:
            if not os.path.isdir(each):
                print('[WARN]Folder {} is not Exist. Creating...'.format(each))
                os.mkdir(each)
        check_file_list = [
            'config/engine.ini',
            'config/game.ini'
        ]
        for each in check_file_list:
            if not os.path.isfile(each):
                print('[WARN]File {} is not Exist. Creating...'.format(each))
                open(each, 'w')

    def load_config(self, config_path):
        config = self.load_data(config_path)
        self.data['config.engine'] = config['config.engine']

    def scan(self, folderName):
        fileList = []
        for root, dirs, files in os.walk(folderName):
            for each in files:
                fileList.append(root + '\\' + each)
        return fileList

    def scan_plugin(self):
        plugin_path_list = self.scan('plugin')
        print('Found {} Plugins...'.format(
            len(plugin_path_list)), end='')
        self.data['plugin'] = plugin_path_list
        return self.scan('plugin')

    def save_to(self, save_num):
        pass

    def load_from(self, saveFile):
        print('load_save', saveFile)

    def add(self, item):
        item['hash'] = new_hash()
        self.pool.append(item)
        return item['hash']

    def get(self, pattern):
        # 参考GraphQL的部分实现原理
        def match(item, pattern):
            found = True
            for each_key in pattern.keys():
                if not each_key in item.keys():
                    found = False
                    break
            if found:
                for each_key in pattern.keys():
                    if isinstance(pattern[each_key], dict):
                        if not match(item[each_key], pattern[each_key]):
                            found = False
                            break
                    elif not pattern[each_key] == item[each_key]:
                        found = False
                        break
                if found:
                    return True
            return False

        candidate_item = []
        for each in self.pool:
            if match(each, pattern):
                candidate_item.append(each)
        return candidate_item

    def load_data(self, files):
        data = {}
        for each in files:
            each = each.replace('/', '\\')
            key = '.'.join('.'.join(each.split('.')[0:-1]).split('\\'))
            ext = each.split('\\')[-1].split('.')[-1]
            # 载入文件
            if ext in ['cfg', 'ini', 'inf', 'config']:
                config = configparser.ConfigParser()
                config.read(each)
                d = dict(config._sections)
                # print(d)
                for k in d:
                    d[k] = dict(d[k])
                data[key] = d
            elif ext == 'csv':
                with open(each, newline='', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    new_list = []
                    for row in reader:
                        new_list.append(row)
                    data[key] = new_list
            elif ext == 'json':
                with open(each, 'r', encoding='utf-8') as f:
                    data[key] = json.loads(''.join(f.readlines()))
        return data


class SocketEngine(DataEngine):
    HOST = 'localhost'
    PORT = 11994
    _conn = None
    _cmd_list = []
    _gui_list = []
    isConnected = False

    def parse_bag(self, bag):
        pass

    def connect(self):
        def core():
            while True:
                data = self.recv()
                for each in data:
                    self.parse_bag(each)

        def func_connect():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
                self._conn = c
                try:
                    self._conn.connect((HOST, PORT))
                    self.isConnected = True
                    print('Connected...', end='')
                    core()
                except OSError as err:
                    if err.errno == 10061:
                        print('[WARN]前端未启动！')
                    else:
                        print(err)

        t = threading.Thread(name='func_connect', target=func_connect)
        t.start()
        while True:
            if self.isConnected:
                break
            time.sleep(0.1)

    def send_config(self):
        bag = {
            'type': 'init',
            'value': {
                'resolution': (800, 600)},
            'from': 'b',
            'to': 'm'
        }
        self.send(bag)

    def send_loaded(self):
        bag = {
            'type': 'loaded',
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)

    def send(self, bag):
        print("[DEBG]发送：", bag)
        self._conn.send(json.dumps(bag, ensure_ascii=False).encode())

    def recv(self):
        data = self._conn.recv(4096)
        print("[DEBG]接收：", data)
        if not data:
            return
        data = data.decode().split('}{')
        for i in range(len(data)):
            if not i == 0:
                data[i] = '}' + data[i]
            if not i == len(data) - 1:
                data[i] = data[i] + '}'
        for i, each in enumerate(data):
            data[i] = json.loads(each)
        return data


class LockEngine(SocketEngine):
    # lock 机制：
    # _lock_status 是指示当前 lock 状态的变量；
    # 0：无锁，可锁（默认）；1：有锁，可解锁；-1：无锁，不可锁；
    #  0：_unlock()        ：与 RENDERER 握手完成，鼠标左键，b；
    #  1：_lock()          ：开始游戏脚本前，p.wait；
    # -1：_unlock_forever()：鼠标右键；
    _lock_status = [0, 'mouse']

    def wait_for_unlock(self):
        # print('wait_for_unlock')
        while self.is_locked():
            time.sleep(0.1)

    def is_locked(self):
        # print('is_locked')
        if self._lock_status[0] == 1:
            return True
        else:
            return False

    def lock_passed(self):
        # print('lock_passed')
        if self._lock_status[0] == -1:
            return True
        else:
            return False

    def lock(self):
        # print('lock')
        self._lock_status[0] = 1

    def unlock(self):
        # print('unlock')
        self._lock_status[0] = 0

    def unlock_forever(self):
        # print('unlock_forever')
        self._lock_status[0] = -1


class BagEngine(LockEngine):
    _cmd_list = []
    _gui_list = []

    def parse_bag(self, bag):
        def parse(bag):
            if bag['type'] == 'MOUSE_CLICK':
                if bag['value'] == 1:  # 左键
                    if self.is_locked:
                        self.unlock()
                elif bag['value'] == 3:  # 右键
                    if self.is_locked:
                        self.unlock_forever()
            elif bag['type'] == 'BUTTON_CLICK':
                for each in self._cmd_list:
                    if bag['value'] == each[0]:
                        each[1](*each[2], **each[3])

        t = threading.Thread(target=parse, args=(bag, ))
        t.start()

    def title(self, text):
        bag = {
            'type': 'title',
            'value': text,
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)

    def t(self, text='', wait=False):
        bag = {'type': 't',
               'value': text,
               'from': 'b',
               'to': 'r'}
        self.send(bag)
        if wait and not self.lock_passed():
            self.lock()
            self.wait_for_unlock()

    def b(self, text, func, *arg, **kw):
        hash = new_hash()
        self._cmd_list.append((hash, func, arg, kw))
        bag = {
            'type': 'b',
            'value': {
                'text': text,
                'hash': hash
            },
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)
        self.unlock()

    def h(self, text, rank=1):
        bag = {
            'type': 'h',
            'value': {
                'text': text,
                'rank': rank
            },
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)

    def page(self):
        bag = {
            'type': 'page',
            'from': 'b',
            'to': 'r'
        }
        self.send(bag)
        global _cmd_list
        self._cmd_list.clear()

    def goto(self, func, *arg, **kw):
        # print('goto:', func.__name__)
        self._gui_list.append((func, arg, kw))
        func(*arg, **kw)

    def back(self, *arg, **kw):
        # print('back')
        self._gui_list.pop()
        repeat()

    def repeat(self, *arg, **kw):
        # TODO(miswanting): RecursionError: maximum recursion depth exceeded
        # print('repeat:', self._gui_list[-1][0].__name__)
        self._gui_list[-1][0](*self._gui_list[-1][1], **self._gui_list[-1][2])


# 核心技术
HOST = 'localhost'
PORT = 11994
_conn = None
_lock_status = [0, 'mouse']
_cmd_list = []
_gui_list = []


def init():
    _fix_path()
    _connect_server()
    _lock()
    _wait_for_unlock()


def init_done():
    bag = {'type': 'LOAD_DONE', 'from': 'b', 'to': 'r'}
    _send(bag)


def title(text):
    bag = {'type': 'title', 'from': 'b', 'to': 'r', 'value': text}
    _send(bag)


def t(text='', wait=False):
    bag = {'type': 't', 'from': 'b', 'to': 'r', 'value': text}
    _send(bag)
    if wait and not _lock_passed():
        _lock()
        _wait_for_unlock()


def b(text, func, *arg, **kw):
    global _cmd_list
    hash = _get_hash()
    _cmd_list.append((hash, func, arg, kw))
    bag = {
        'type': 'b',
        'from': 'b',
        'to': 'r',
        'value': {
            'text': text,
            'hash': hash
        }
    }
    _send(bag)
    _unlock()


def h(text, rank=1):
    bag = {
        'type': 'h',
        'from': 'b',
        'to': 'r',
        'value': {
            'text': text,
            'rank': rank
        }
    }
    _send(bag)


def progress(now, max=100, length=100):
    bag = {
        'type': 'progress',
        'from': 'b',
        'to': 'r',
        'value': {
            'now': now,
            'max': max,
            'length': length
        }
    }
    _send(bag)


def input(text=''):
    package = {'type': 'input', 'value': text}
    _send(package)
    _lock('input')
    _wait_for_unlock()


def page():
    bag = {'type': 'page', 'from': 'b', 'to': 'r'}
    _send(bag)
    global _cmd_list
    _cmd_list.clear()


def goto(func, *arg, **kw):
    _gui_list.append((func, arg, kw))
    func(*arg, **kw)


def back(*arg, **kw):
    _gui_list.pop()
    repeat()


def repeat(*arg, **kw):
    _gui_list[-1][0](*_gui_list[-1][1], **_gui_list[-1][2])


def mode(value='plain', *arg, **kw):
    bag = {'type': 'mode', 'from': 'b', 'to': 'r', 'value': [value, arg, kw]}
    _send(bag)


def clear():
    bag = {'type': 'clear', 'from': 'b', 'to': 'r'}
    _send(bag)


def _______________________________________________________():
    pass


# lock 机制：
# _lock_status 是指示当前 lock 状态的变量；
# 0：无锁，可锁（默认）；1：有锁，可解锁；-1：无锁，不可锁；
#  0：_unlock()        ：与 RENDERER 握手完成，鼠标左键，b；
#  1：_lock()          ：开始游戏脚本前，p.wait；
# -1：_unlock_forever()：鼠标右键；
def _wait_for_unlock():
    global _lock_status
    while _lock_status[0] == 1:
        time.sleep(0.1)


def _is_locked():
    global _lock_status
    if _lock_status[0] == 1:
        return True
    else:
        return False


def _lock_passed():
    global _lock_status
    if _lock_status[0] == -1:
        return True
    else:
        return False


def _lock(lock_type='mouse'):
    global _lock_status
    _lock_status = [1, lock_type]


def _unlock(lock_type='mouse'):
    global _lock_status
    if lock_type == _lock_status[1]:
        _lock_status = [0, lock_type]


def _unlock_forever(lock_type='mouse'):
    global _lock_status
    if lock_type == _lock_status[1]:
        _lock_status = [-1, lock_type]


def _get_hash():
    m = hashlib.md5()
    m.update(str(random.random()).encode("utf-8"))
    return m.hexdigest().upper()


def _fix_path():
    if getattr(sys, 'frozen', False):
        # frozen
        dir_ = os.path.dirname(sys.executable)
        gamepath = os.path.dirname(dir_)
    else:
        # unfrozen
        dir_ = os.path.dirname(os.path.realpath(__file__))
        gamepath = os.path.dirname(os.path.dirname(dir_))
    sys.path.append(gamepath)


def _connect_server():
    t = threading.Thread(name='socket', target=_connect)
    t.start()


def _connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        global _conn
        _conn = c
        try:
            _conn.connect((HOST, PORT))
            print('[DONE]已连接上 MAIN ！')
        except OSError as err:
            if err.errno == 10061:
                print('[WARN]前端未启动！')
            else:
                print(err)
        # 传输客户端信息
        print('[DEBG]开始与 MAIN 握手…')
        syn = {'type': 'syn', 'from': 'b', 'to': 'm'}
        _send(syn)
        while True:
            data = _conn.recv(4096)
            print("[DEBG]接收：", data)
            if not data:
                continue
            data = data.decode().split('}{')
            for i in range(len(data)):
                if not i == 0:
                    data[i] = '}' + data[i]
                if not i == len(data) - 1:
                    data[i] = data[i] + '}'
            for each in data:
                bag = json.loads(each)
                if bag['type'] in ['exit', 'quit', 'close']:
                    print("[DEBG]服务器即将关闭！")
                    break
                _parse_bag(bag)


def _send(bag):
    print("[DEBG]发送：", bag)
    _conn.send(json.dumps(bag, ensure_ascii=False).encode())


def _parse_bag(bag):
    def parse(bag):
        if bag['type'] == 'ack':
            pass
        elif bag['type'] == 'syn':
            ack = {'type': 'ack', 'from': 'b', 'to': bag['from'], 'value': bag}
            _send(ack)
            if bag['from'] == 'm':
                print('[DONE]与 MAIN 握手完成！')
                print('[DEBG]开始与 RENDERER 握手…')
                syn = {'type': 'syn', 'from': 'b', 'to': 'r'}
                _send(syn)
            elif bag['from'] == 'r':
                print('[DONE]与 RENDERER 握手完成！')
                _unlock()
        elif bag['type'] == 'MOUSE_CLICK':
            if bag['value'] == 1:  # 左键
                if _is_locked:
                    _unlock()
            elif bag['value'] == 3:  # 右键
                if _is_locked:
                    _unlock_forever()
        elif bag['type'] == 'BUTTON_CLICK':
            for each in _cmd_list:
                if bag['value'] == each[0]:
                    each[1](*each[2], **each[3])

    t = threading.Thread(target=parse, args=(bag, ))
    t.start()


class Engine(BagEngine):
    pass
