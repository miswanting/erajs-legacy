# import configparser
# import os
# import sys
# from pathlib import Path

# from .. import LogManager
from . import DataManager, LockManager, ProtocolManager
from .. import Tools


class APIManager(DataManager.DataManager, LockManager.LockManager, ProtocolManager.ProtocolManager):
    def __init__(self):
        super().__init__()

    def config(self, data: dict) -> None:  # 新特性：设置引擎
        pass

    def exit(self, quick_save: bool = False) -> None:  # 退出引擎
        pass

    # 显示方法
    def push(self, widget) -> object:  # 新特性：推送控件

        return

    # # 显示控件
    # def page(self, color: str = 'default') -> None:  # 控件：页面
    #     pass

    def title(self, text: str) -> None:  # 设置游戏窗口标题
        bag = self.get_bag('title')
        bag['value'] = str(text)
        self.send(bag)

    def page(self, color: str = 'default'):
        bag = self.get_bag('page')
        bag['value'] = {
            'color': color
        }
        self.send(bag)
        self.remove_all_listeners()
        self.mode()

    def header(self, text: str, rank: int = 1, color: str = 'default', bcolor: str = 'default') -> None:  # 控件：标题
        bag = self.get_bag('h')
        bag['value'] = {
            'text': str(text),
            'rank': rank,
            'color': color,
            'bcolor': bcolor
        }
        self.send(bag)

    def text(self, text: str = '', wait: bool = False, color: str = 'default', bcolor: str = 'default', style=None) -> None:  # 控件：文字
        bag = self.get_bag('t')
        bag['value'] = {
            'text': str(text),
            'color': color,
            'bcolor': bcolor
        }
        self.send(bag)

        if wait and not self.lock_passed():
            def handle_lock(e):
                print(e)
                if e['value'] == 1:  # 左键
                    if self.is_locked:
                        self.unlock()
                elif e['value'] == 3:  # 右键
                    if self.is_locked:
                        self.unlock_forever()
            self.on('MOUSE_CLICK', handle_lock)
            self.lock()
            self.wait_for_unlock()

    def link(self, text: str, callback: callable, *arg, **kw) -> None:  # 控件：链接
        hash = Tools.random_hash()
        bag = self.get_bag('l')
        bag['value'] = {
            'text': str(text),
            'hash': hash
        }
        bag['value']['disabled'] = False
        if 'disabled' in kw.keys():
            if kw['disabled']:
                bag['value']['disabled'] = True
            kw.pop('disabled')
        if callback == None:
            bag['value']['disabled'] = True
        if 'popup' in kw.keys():
            bag['value']['popup'] = str(kw['popup'])
            kw.pop('popup')
        else:
            bag['value']['popup'] = ''
        if 'color' in kw.keys():
            bag['value']['color'] = kw['color']
            kw.pop('color')
        else:
            bag['value']['color'] = ''

        def handle_callback(e):
            if e['hash'] == hash:
                callback(*arg, **kw)
        self.add_listener('LINK_CLICK', handle_callback)
        # self._cmd_list.append((hash, func, arg, kw))
        self.send(bag)
        self.unlock()

    l = link

    def button(self, text: str, callback: callable, *arg, **kw) -> None:  # 控件：按钮
        hash = Tools.random_hash()
        bag = self.get_bag('b')
        bag['value'] = {
            'text': str(text),
            'hash': hash
        }
        bag['value']['disabled'] = False
        if 'disabled' in kw.keys():
            if kw['disabled']:
                bag['value']['disabled'] = True
            kw.pop('disabled')
        if callback == None:
            bag['value']['disabled'] = True
        if 'isLink' in kw.keys():
            if kw['isLink']:
                bag['value']['isLink'] = True
            kw.pop('isLink')
        if 'popup' in kw.keys():
            bag['value']['popup'] = str(kw['popup'])
            kw.pop('popup')
        else:
            bag['value']['popup'] = ''
        if 'color' in kw.keys():
            bag['value']['color'] = kw['color']
            kw.pop('color')
        else:
            bag['value']['color'] = ''

        def handle_callback(e):
            if e['hash'] == hash:
                callback(*arg, **kw)
        self.add_listener('BUTTON_CLICK', handle_callback)
        # self._cmd_list.append((hash, func, arg, kw))
        self.send(bag)
        self.unlock()

    def divider(self, text: str = ''):
        bag = self.get_bag('divider')
        bag['value'] = str(text)
        self.send(bag)

    def progress(self, now: int,  max: int = 100, length: int = 100) -> object:  # 控件：进度条
        bag = self.get_bag('progress')
        bag['value'] = {
            'now': now,
            'max': max,
            'length': length
        }
        self.send(bag)

    def rate(self, now: int = 0,  max: int = 5, callback: callable = None, disabled: bool = True) -> object:  # 控件：评分
        hash = Tools.random_hash()

        def handle_callback(e):
            if e['target'] == hash:
                callback(e['value'])
        bag = self.get_bag('rate')
        bag['value'] = {
            'now': now,
            'max': max,
            'hash': hash,
            'disabled': disabled
        }
        self.send(bag)

    def check(self, *arg, **kw):
        print('Deprecated API: check is not used anymore. Please use checkbox instead.')
        self.checkbox(*arg, **kw)

    def checkbox(self, text='', callback: callable = None, *arg, **kw):
        hash = Tools.random_hash()

        def handle_callback(e):
            if e['target'] == hash:
                callback(e['value'])
        self.on('CHECK_CHANGE', handle_callback)
        bag = self.get_bag('checkbox')
        bag['value'] = {
            'text': str(text),
            'hash': hash
        }
        if 'disabled' in kw.keys():
            if kw['disabled']:
                bag['value']['disabled'] = True
            kw.pop('disabled')
        if callback == None:
            bag['value']['disabled'] = True

        bag['value']['default'] = False
        if 'default' in kw.keys():
            bag['value']['default'] = kw['default']
            kw.pop('default')
        if 'read_only' in kw.keys():
            bag['value']['read_only'] = kw['read_only']
            kw.pop('read_only')
        self.send(bag)

    def radio(self, options, callback: callable = None, default: int = 0):
        hash = Tools.random_hash()

        def handle_callback(e):
            if e['target'] == hash:
                callback(e['value'])
        self.on('RADIO_CLICK', handle_callback)
        bag = self.get_bag('radio')
        bag['value'] = {
            'list': options,
            'default': default,
            'hash': hash
        }
        self.send(bag)

    def input(self, callback: callable = None, default: any = None, is_area=False, placeholder: str = ''):
        hash = Tools.random_hash()

        def handle_callback(e):
            if e['hash'] == hash:
                callback(e['value'])
        self.on('INPUT_CHANGE', handle_callback)
        bag = self.get_bag('input')
        bag['value'] = {
            'hash': hash,
            'default': str(default),
            'is_area': is_area,
            'placehoder': str(placeholder)
        }
        self.send(bag)

    def dropdown(
        self,
        options,
        callback: callable = None,
        default: any = None,
        search: bool = False,
        multiple: bool = False,
        placeholder: str = '',
        allowAdditions: bool = False
    ):
        hash = Tools.random_hash()

        def handle_callback(e):
            if e['target'] == hash:
                callback(e['value'])
        self.on('DROPDOWN_CHANGE', handle_callback)
        bag = self.get_bag('dropdown')
        bag['value'] = {
            'hash': hash,
            'options': options,
            'default': default,
            'search': search,
            'multiple': multiple,
            'placeholder': str(placeholder),
            'allowAdditions': allowAdditions
        }
        self.send(bag)
    # def radio(self, choice_list: list, default_index: int = 0, func: callable = None) -> None:  # 控件：单选
    #     pass

    # def checkbox(self, check_dict_or_list: dict, func: callable = None) -> None:  # 控件：多选
    #     pass

    # def input(self, func: callable = None, default: str = '') -> None:  # 控件：输入
    #     pass

    # def dropdown(self, options: list, func: callable = None, default: str = '', search: bool = False, multiple: bool = False, placeholder: str = '', allowAdditions: bool = False) -> None:  # 控件：下拉菜单
    #     pass

    # def divider(self, text: str = '') -> None:  # 控件：水平分割线
    #     pass

    # def clear(self, num: int = 0) -> None:  # 控件：清除显示页面
    #     pass

    # 显示功能

    def shake(self, duration: int = 500) -> None:  # 功能：页面震动（原窗口震动）
        pass

    def mode(self, type: str = 'default', *arg, **kw) -> None:  # 功能：改变控件显示模式
        pass

    # 页面逻辑控制
    def goto(self, func: callable, *arg, **kw) -> None:  # 页面控制：进入到新页面
        self.debug('GOTO: Append [{}] to [{}] & run'.format(
            func.__name__, self._show_gui_list()))
        self._gui_list.append((func, arg, kw))  # append_gui
        func(*arg, **kw)

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
