# coding:utf-8
from . import game as g

# from . import engine as e
# init = g.init
# init_done = g.init_done
# title = g.title
# t = g.t
# b = g.b
# h = g.h
# progress = g.progress
# input = g.input
# page = g.page
# goto = g.goto
# back = g.back
# repeat = g.repeat
# mode = g.mode
# clear = g.clear


# 显示控制
def init():
    g.init()


def title(text):
    g.title(text)


def t(text='', wait=False):
    g.t(text, wait)


def b(text, func, *arg, **kw):
    g.b(text, func, *arg, **kw)


def h(text):
    g.h(text)


def progress():
    pass


def input():
    pass


def page():
    g.page()


def goto(func, *arg, **kw):
    g.goto(func, *arg, **kw)


def back(*arg, **kw):
    g.back(*arg, **kw)


def repeat(*arg, **kw):
    g.repeat(*arg, **kw)


def mode():
    pass


def clear():
    pass


# 资源控制
def get():
    pass


def ________________________________________________________________():
    pass
