# coding:utf-8
from . import engine as e

# 游戏平台
data = {}  # 静态数据
db = {}  # 动态数据
pool = {}

engine = e.Engine()


def init():
    print('[DEBG]Initializing...')
    print('[DEBG]Fixing Path...', end='')
    engine.fix_path()
    print('OK')
    print('[DEBG]Checking Program Integrity...', end='')
    engine.self_check()
    print('OK')
    print('[DEBG]Loading Engine Configuration...', end='')
    engine.load_config(['config/config.ini'])
    print('OK')
    print('[DEBG]Register API...', end='')
    engine.register_api()
    print('OK')
    print('[DEBG]Scanning Plugins...', end='')
    engine.scan_plugin()
    print('OK')
    print('[DEBG]Loading Plugins...')
    engine.load_plugin()
    print('OK')
    print('[DEBG]Connecting Server...', end='')
    engine.connect()
    print('OK')
    print('[DEBG]Transfering Configuration to Server...')
    engine.send_config()
    print('OK')
    print('[DEBG]Scanning Core Files...', end='')
    print('OK')
    print('[DEBG]Loading Core Files...', end='')
    print('OK')
    print('[DEBG]Scanning DLCs...', end='')
    print('OK')
    print('[DEBG]Loading DLCs...', end='')
    print('OK')
    print('[DEBG]Scanning MODs...', end='')
    print('OK')
    print('[DEBG]Loading MODs...', end='')
    print('OK')
    print('[DEBG]Transferring Loading Complete Signal...')
    engine.send_loaded()
    print('OK')
    print('[FINE]Initialize Complete!')
    return engine.data


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


def clear_gui():
    engine.clear_gui()


def show_save_to_save():
    def save_to(save_num):
        engine.save_to(save_num)
        engine.repeat()
    # 获取列表
    save_file_list = engine.scan('save')
    # print(save_file_list)
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
        elif int(save_file_list[0].split('\\')[-1].split('.')[0]) == current_num:
            save_list.append((current_num, str(current_num)))
            save_file_list = save_file_list[1:]
            current_num += 1
    # 显示
    for each in save_list:
        engine.b(str(each[0])+'. '+each[1], save_to, each[0])
        engine.t()
    # 处理
    pass


def show_save_to_load(func_after_load):
    def load_from(save_num):
        engine.load_from(save_num)
        engine.clear_gui()
        engine.goto(func_after_load)
    # 获取列表
    save_file_list = engine.scan('save')
    # 弱加载
    for each in save_file_list:
        pass
    # 计算显示
    save_list = []
    for each in save_file_list:
        save_list.append((int(each.split('\\')[-1].split('.')[0]), ''))
    # 显示
    for each in save_list:
        engine.b(str(each[0])+'. '+each[1], load_from, each[0])
        engine.t()
    # 处理
    pass


def save(filename):
    pass


def load_save(filename):
    pass


def add(item):
    return engine.add(item)


def get(pattern):
    return engine.get(pattern)


def get_full_time():
    return engine.data['api']['get_full_time']()


def tick():
    engine.data['api']['tick']()


def _______________________________________________________():
    pass
