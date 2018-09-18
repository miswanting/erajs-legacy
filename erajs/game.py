# coding:utf-8
from . import bios as b
from . import engine as e

# 游戏平台
data = {}  # 静态数据
db = {}  # 动态数据

engine = e.Engine()


def init():
    fileList = b.init()
    print(fileList)
    engine.load_data(fileList['plugin'])
    engine.load_data(fileList['config'])
    engine.load_data(fileList['game'])
    engine.load_data(fileList['dlc'])
    engine.load_data(fileList['save'])
    engine.connect()


def title(text):
    bag = {'type': 'title', 'value': text, 'from': 'b', 'to': 'r'}
    engine.send(bag)


def save(filename):
    pass


def load_save(filename):
    pass


def _______________________________________________________():
    pass
