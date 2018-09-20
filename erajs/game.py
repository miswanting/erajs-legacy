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
    # 获取列表
    save_file_list = engine.scan('save')
    print(save_file_list)
    # 弱加载
    for each in save_file_list:
        pass
    # 计算显示
    save_list = []
    current_num = 1
    while True:
        if len(save_file_list) == 0:
            save_list.append((current_num, '未使用'))
            break
    # 显示
    for each in save_list:
        engine.b(str(each[0])+'. '+each[1], engine.save_to, each[0])
        engine.t()
    # 处理
    pass


def show_save_to_load():
    pass


def save(filename):
    pass


def load_save(filename):
    pass


def _______________________________________________________():
    pass
