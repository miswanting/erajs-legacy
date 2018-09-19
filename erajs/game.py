# coding:utf-8
from . import bios as bios
from . import engine as e

# 游戏平台
data = {}  # 静态数据
db = {}  # 动态数据

engine = e.Engine()


def init():
    print('[DEBG]正在初始化...')
    fileList = bios.init()
    print('[DEBG]正在加载插件...', end='')
    engine.load_data(fileList['plugin'])
    print('OK')
    print('[DEBG]正在读取配置文件...', end='')
    engine.load_data(fileList['config'])
    print('OK')
    print('[DEBG]正在连接服务器...')
    engine.connect()
    print('[DEBG]正在加载游戏核心...', end='')
    engine.load_data(fileList['game'])
    print('OK')
    print('[DEBG]正在加载可下载内容（DLC）...', end='')
    engine.load_data(fileList['dlc'])
    print('OK')
    print('[DEBG]正在加载存档...', end='')
    engine.load_data(fileList['save'])
    print('OK')
    engine.send({'type': 'loaded', 'from': 'b', 'to': 'r'})
    print('[FINE]加载完毕！')


def title(text):
    engine.title(text)


def t(text='', wait=False):
    engine.t(text, wait)


def b(text, func, *arg, **kw):
    engine.b(text, func, *arg, **kw)


def h(text, rank=1):
    engine.h(text, rank)


def page():
    engine.page()


def goto(func, *arg, **kw):
    engine.goto(func, *arg, **kw)


def back(*arg, **kw):
    engine.back(*arg, **kw)


def repeat(*arg, **kw):
    engine.repeat(*arg, **kw)


def show_save_to_save():
    pass


def show_save_to_load():
    pass


def save(filename):
    pass


def load_save(filename):
    pass


def _______________________________________________________():
    pass
