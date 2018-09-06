# coding:utf-8
import erajs.era as e


def start_new_game():
    e.page()
    e.h('玩家角色创建方式')
    e.t()
    e.t()
    e.b('使用默认主角', e.goto, default_person)


def default_person():
    e.page()
    e.h('默认玩家角色')
    e.t()
    e.t()


e.init()
e.init_done()
e.title('EraLife')
e.h('EraLife')
e.t()
e.t()
e.b('新建游戏', e.goto, start_new_game)
