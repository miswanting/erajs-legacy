# coding:utf-8

# 自有库
from . import DataManager
from . import EventManager
from . import LogManager
from . import ModuleManager
from . import NetManager
from . import LockManager
from . import BagManager
from . import Prototypes


# 设计第一，架构第二，技术第三，实现第四
# 多快好省，力争上游，为开发世界一流游戏引擎而奋斗


class Engine(Prototypes.Singleton):
    VERSION: str = '0.1.0-191026'

    def __init__(self) -> None:  # 架构初始化
        self.log = LogManager.LogManager()  # 调试框架
        self.data = DataManager.DataManager()  # 数据管理
        self.event = EventManager.EventManager()  # 基本事件框架
        self.lock = LockManager.LockManager()  # 锁管理框架
        self.module = ModuleManager.ModuleManager()  # 模块管理
        self.net = NetManager.NetManager()  # 网络管理
        self.bag = BagManager.BagManager()  # 通信协议管理

    def config(self, data: dict) -> None:  # 新特性：设置引擎
        pass

    def exit(self, quick_save: bool = False) -> None:  # 退出引擎
        pass

    # 显示方法
    def push(self, widget) -> None:  # 新特性：推送控件
        pass

    # 显示控件
    def page(self, color: str = 'default') -> None:  # 控件：页面
        pass

    def title(self, text: str) -> None:  # 设置游戏窗口标题
        pass

    def t(self, text: str = '', wait: bool = False, color: str = 'default', bcolor: str = 'default') -> None:  # 控件：文字
        pass

    def l(self, text: str, func: callable, *arg, **kw) -> None:  # 控件：链接
        pass

    def b(self, text: str, func: callable, *arg, **kw) -> None:  # 控件：按钮
        pass

    def h(self, text: str, rank: int = 1, color: str = 'default', bcolor: str = 'default') -> None:  # 控件：标题
        pass

    def progress(self, now: int,  max: int = 100, length: int = 100) -> None:  # 控件：进度条
        pass

    def rate(self, now: int = 0,  max: int = 5, func: callable = None, disabled: bool = True) -> None:  # 控件：评分
        pass

    def radio(self, choice_list: list, default_index: int = 0, func: callable = None) -> None:  # 控件：单选
        pass

    def checkbox(self, check_dict_or_list: dict, func: callable = None) -> None:  # 控件：多选
        pass

    def input(self, func: callable = None, default: str = '') -> None:  # 控件：输入
        pass

    def dropdown(self, options: list, func: callable = None, default: str = '', search: bool = False, multiple: bool = False, placeholder: str = '', allowAdditions: bool = False) -> None:  # 控件：下拉菜单
        pass

    def divider(self, text: str = '') -> None:  # 控件：水平分割线
        pass

    def clear(self, num: int = 0) -> None:  # 控件：清除显示页面
        pass

    # 显示功能
    def shake(self, duration: int = 500) -> None:  # 功能：页面震动（原窗口震动）
        pass

    def mode(self, type: str = 'default', *arg, **kw) -> None:  # 功能：改变控件显示模式
        pass

    # 页面逻辑控制
    def goto(self, func: callable, *arg, **kw) -> None:  # 页面控制：进入到新页面
        pass

    def back(self, num: int = 1, *arg, **kw) -> None:  # 页面控制：退出到原页面
        pass

    def repeat(self, *arg, **kw) -> None:  # 页面控制：重绘当前页面（新增）
        pass

    def refresh(self, *arg, **kw) -> None:  # 页面控制：重绘当前页面（刷新）
        pass

    def append_gui(self, func: callable, *arg, **kw) -> None:  # 页面控制：追加页面（弃用）
        pass

    def append_node(self, func: callable, *arg, **kw) -> None:  # 页面控制：追加页面节点（替代append_gui）
        pass

    def clear_gui(self, num: int = 0) -> None:  # 页面控制：移除页面（弃用）
        pass

    def remove_node(self, num: int = 0) -> None:  # 页面控制：移除页面节点（替代clear_gui）
        pass

    def get_gui_list(self) -> None:  # 返回当前节点名称（弃用）
        pass

    def _show_gui_list(self) -> None:  # 返回当前节点名称（弃用）
        pass

    def get_node_list(self) -> None:  # 返回当前节点名称（替代get_gui_list）
        pass

    # 引擎功能
    def generate_map(self):  # 引擎功能：生成世界地图
        pass


if __name__ == '__main__':
    e = Engine()
    e.init()
