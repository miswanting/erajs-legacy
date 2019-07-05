from typing import Any, Callable
from . import NEngine

e = NEngine.Engine()


# 【【【【【【【【【【系统方法】】】】】】】】】】
def init() -> None:
    return e.init()


# 【【【【【【【【【【调试方法】】】】】】】】】】
def debug(*arg) -> None:
    pass


def info(*arg) -> None:
    pass


def warn(*arg) -> None:
    pass


def error(*arg) -> None:
    pass


# 【【【【【【【【【【窗口方法】】】】】】】】】】
def title(text: Any) -> None:
    pass


# 【【【【【【【【【【行内控件】】】】】】】】】】
def text(text: Any, callback: Callable = None) -> object:
    return object


def link(text: Any, callback: Callable = None) -> object:
    return object


def button(text: Any, callback: Callable = None) -> object:
    return object

# TODO:h控件考虑取消


def rate(now: int = 0, callback: Callable = None) -> object:
    print('警告：该API有变动！')
    return object


def progress() -> object:
    pass


def check() -> object:
    pass


def radio() -> object:
    pass


def input() -> object:
    pass


def dropdown() -> object:
    pass


# 【【【【【【【【【【块级控件】】】】】】】】】】
def divider() -> object:
    pass


def chart() -> object:
    pass


# 【【【【【【【【【【页级控件】】】】】】】】】】
def page() -> object:
    pass


# 【【【【【【【【【【窗级控件】】】】】】】】】】
# 【【【【【【【【【【全屏控件】】】】】】】】】】
# 【【【【【【【【【【整体构筑】】】】】】】】】】
def push(component, data) -> object:
    pass


# 【【【【【【【【【【界面逻辑】】】】】】】】】】
def clear(num: int = 0) -> object:
    pass


def goto(func, *arg, **kw) -> object:
    pass


def back(func, *arg, **kw) -> object:
    pass


def repeat(func, *arg, **kw) -> object:
    pass


def clear_gui(func, *arg, **kw) -> object:
    pass


def append_gui(func, *arg, **kw) -> object:
    pass


def get_gui_list(func, *arg, **kw) -> object:
    pass


# 【【【【【【【【【【样式控制】】】】】】】】】】
def get_default_style_by_component() -> None:
    pass


# 【【【【【【【【【【界面预设】】】】】】】】】】
def show_save_to_save() -> None:
    pass


def show_save_to_load() -> None:
    pass


# 【【【【【【【【【【别名定义】】】】】】】】】】
t = text
l = link
b = button

if __name__ == "__main__":
    e.init()
# 整体构筑特性 示例代码
# 一次生成含有三行文本的单独页面
e.push(
    e.page, {
        'item': [
            (e.line, {
                'item': [
                    (e.text, {
                        'value': '第1行 第1段文字'
                    }),
                    (e.text, {
                        'value': '第1行 第2段文字'
                    })
                ]
            }),
            (e.line, {
                'item': [
                    (e.text, {
                        'value': '第2行 第1段文字'
                    })
                ]
            }),
            (e.line, {
                'item': [
                    (e.text, {
                        'value': '第3行 第1段文字'
                    })
                ]
            }),
        ]
    }
)
