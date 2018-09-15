# coding:utf-8
from . import bios as b
from . import engine as e

# 游戏平台
data = {}  # 静态数据
db = {}  # 动态数据


def init():
    fileList = b.init()
    print(fileList)
    engine = e.Engine()
    engine.load_data(fileList)
    engine.connect()


def save(filename):
    pass


def load_save(filename):
    pass


def _______________________________________________________():
    pass
