# coding:utf-8
import erajs.NAPI as a


def cover():
    a.title('EraLife')
    a.h('EraLife')
    a.t()
    a.t()
    a.b('新建游戏', a.goto, start_new_game)


def start_new_game():
    a.page()
    a.h('玩家角色创建方式')
    a.t()
    a.t()
    a.b('使用默认主角', a.goto, default_person)


def default_person():
    a.page()
    a.h('默认玩家角色')
    a.t()
    a.t()


if __name__ == "__main__":
    a.config()
    a.init()
    a.goto(cover)
