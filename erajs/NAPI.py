from typing import Any, Callable, Dict

from . import NMID as m

__API_VERSION__ = '0.1.0-191115'


# 系统输出
def debug(*arg) -> None:
    """
    # 【调试级】标准输出
    用于输出开发阶段的调试信息；\n
    该级别的调试信息将不会被log收录；\n
    当程序打包之后将会不再显示该类信息。
    ## 用法举例
    ```python
    a.debug("此处变量tmp的值为：{}".format(tmp))
    a.debug("1", "2", "Switch!")
    ```
    """
    return m.print(0, *arg)


def info(*arg) -> None:
    """
    # 【信息级】标准输出
    用于输出面向用户的指示信息；\n
    会被log收录；
    ## 用法举例
    ```python
    a.info("此处变量tmp的值为：{}".format(tmp))
    a.info("1", "2", "Switch!")
    ```
    """
    return m.print(1, *arg)


def warn(*arg) -> None:
    """
    # 【警告级】标准输出
    用于输出面向用户的警告信息；\n
    含义：系统运行存在隐藏风险；\n
    会被log收录；
    ## 用法举例
    ```python
    a.warn("此处变量tmp的值为：{}".format(tmp))
    a.warn("1", "2", "Switch!")
    ```
    """
    print()
    return m.print(2, *arg)


def error(*arg) -> None:
    """
    # 【错误级】标准输出
    用于输出面向用户的错误信息；\n
    含义：系统运行出现非致命的错误；\n
    会被log收录；
    ## 用法举例
    ```python
    a.error("此处变量tmp的值为：{}".format(tmp))
    a.error("1", "2", "Switch!")
    ```
    """
    return m.print(3, *arg)


def critical(*arg) -> None:
    """
    # 【危险级】标准输出
    用于输出面向用户的危险警告信息；\n
    含义：系统运行出现致命错误，系统将在此中断；\n
    会被log收录；
    ## 用法举例
    ```python
    a.critical("此处变量tmp的值为：{}".format(tmp))
    a.critical("1", "2", "Switch!")
    ```
    """
    return m.print(4, *arg)


# 引擎生命周期
def config(**kw) -> None:
    """
    # 配置引擎参数
    用于设置引擎的
    ## 用法
    ```python
    a.config(configFilePath=./log/back.log)
    a.config({"configFilePath": "./log/back.log"})
    ```
    ## 引擎配置分项说明
    - configFilePath：系统日志文件存放路径与文件名
    - scriptIP：脚本服务器绑定IP地址
    - scriptPort：脚本服务器绑定端口地址
    - frontIP：前端服务器绑定IP地址
    - frontPort：前端服务器绑定端口地址
    - serverIP：上位服务器绑定IP地址
    - serverPort：上位服务器绑定端口地址
    - hasFrontServer：是否存在前端服务器
    - hasServer：是否存在上位服务器

    ## 引擎默认配置
    ```json
    {
        "configFileName": "./back.log",
        "scriptIP": "localhost",
        "scriptPort": 11994,
        "frontIP": "localhost",
        "frontPort": 11995,
        "serverIP": "localhost",
        "serverPort": 11995,
        "hasFrontServer": false,
        "hasServer": false
    }
    ```
    """
    return m.config(**kw)


def init() -> None:
    return m.init()


def entry() -> None:
    # return m.entry()
    pass


def go() -> None:
    # return m.go()
    pass


# 数据获取
def std():  # data文件夹中的静态数据，全局引用
    pass


def dat():  # 【旧】data文件夹中的数据文件，全局引用，拆成
    pass


def usr():  # 当前存档的存档数据
    pass


data = m.data  # 缓存数据，动态数据，全局引用
# File
# cfg/: cfg
# data/: std
# cache/: cache
# save/: data, tmp, save
# Data
# Server: cfg + std + cache
# World: data + tmp
# Player: save + ram


# 系统级控件
def title(text: Any) -> None:
    pass


# 窗口级控件
def toast():
    pass


# 容器级控件
def toggle_devtool():
    pass


def toggle_terminal():
    pass


def toggle_menu():
    pass


# 页面级控件
def page():
    pass


# 块级控件
def mode():
    pass


def divider():
    pass


# 行内控件
def header(text: Any, callback: Callable = None) -> object:
    return object


h = header


def text(
    text: str = '',
    wait: bool = False,
    color: str = 'default',
    bcolor: str = 'default',
    style: dict = {}
) -> object:
    """
    # 添加文本控件
    向光标处添加文本控件。
    ## 参数
    - text: str = ""
        - 文本控件所显示的文字；
        - 当该参数值为 "" 时，将光标移往`下一位置`；
            - 当 mode 为 default 时，`下一位置`为下一行；
            - 当 mode 为 grid 时，`下一位置`为下一个单元格；
    - wait: bool = False
        - 添加该文本控件后是否等待。
        - 当该参数值为 True 时，暂停运行脚本，直至用户`点击鼠标`，才会解除暂停状态。
            - 用户点击鼠标左键：解除当前暂停状态，下次遇到要求暂停的脚本依然会暂停；
            - 用户点击鼠标右键：解除当前暂停状态，下次遇到要求暂停的脚本不会暂停，直至新的一页生成。
    - color: str = 'default'
        - 设置文字颜色。（临时级）
        - 支持 CSS3 支持的所有颜色设置方式
            - 支持颜色名："red", "green", "blue" 等；
                - 包括一级、二级和三级颜色名。
                    - 参见：
            - 支持缩写十六进制颜色值："#f00", "#0f0", "#00f" 等；
            - 支持十六进制颜色值："#ff0000", "#00ff00", "#0000ff" 等；
            - 支持 RGB 颜色表达式："rgb(255,0,0)", "rgba(0,255,0,0.5)"；
    - bcolor: str = 'default'
        - 设置文字背景颜色。（临时级）
        - 用法同上。
    - style: dict = {}
        - 样式参数。（临时级）
        - 这用法神奇了。您竟然可以参照 CSS3 中的属性对该控件的样式进行自由设置。
            - 如若要添加绿底红字的文本控件，应传入：
    ```json
    {
        'color': 'red',
        'background-color': 'green'
    }
    ```
    """
    return m.text(text, wait, color, bcolor, style)


t = text


def link(text: Any, callback: Callable = None) -> object:
    return object


l = link


def button(text: Any, callback: Callable = None, *arg, **kw) -> object:
    return object


b = button


def rate(now: int = 0, callback: Callable = None) -> object:
    print('警告：该API有变动！')
    return object


def progress() -> object:
    return object


def check() -> object:
    return object


def radio() -> object:
    return object


def input() -> object:
    return object


def dropdown() -> object:
    return object


# 整体构筑
def push(component, data) -> object:
    pass


def clear(num: int = 0) -> object:
    pass


# 界面逻辑
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


# 样式控制
def get_sys_event_type() -> None:
    pass


def add_listener() -> None:
    pass


def has_listener() -> None:
    pass


def remove_listener() -> None:
    pass


def remove_all_listeners() -> None:
    pass


def dispatch() -> None:
    pass


emit = dispatch


def get_listener_list() -> None:
    pass


# 样式控制
def set_custom_style() -> None:
    pass


def reset_custom_style() -> None:
    pass


def set_style() -> None:
    pass


def reset_style() -> None:
    pass


# 界面预设
def show_save_to_save() -> None:
    pass


def show_save_to_load() -> None:
    pass
