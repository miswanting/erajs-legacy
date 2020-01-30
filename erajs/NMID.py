"""
中间件
"""

import time
import typing

from . import LogManager, NEngine, Widgets, Events
from .Managers import EventManager
e = NEngine.Engine()

logger = LogManager.logger
dispatcher = EventManager.EventDispatcher()
SystemEvent = Events.SystemEvent


def print(level, *argF):
    pass


def config(**kw):
    logger.debug(kw)


def init():
    def change_init_status(e):
        nonlocal is_init_finished
        is_init_finished = True
        dispatcher.remove_all_listeners()
    is_init_finished = False
    e.init()
    dispatcher.once(
        SystemEvent.ENGINE_INIT_FINISHED,
        change_init_status
    )
    dispatcher.emit(SystemEvent.ENGINE_INIT_STARTED)
    while True:
        if is_init_finished:
            break
        time.sleep(1)


def std():
    pass


def data():
    pass


def cache():
    pass


def save():
    pass


def text(
    text: str = '',
    wait: bool = False,
    color: str = 'default',
    bcolor: str = 'default',
    style: dict = None
):
    """
    # 文字控件
    """
    # 组装数据
    data = {
        'text': text,
        'wait': wait,
        'style': style
    }
    if color != 'default':
        data['style']['color'] = color
    if bcolor != 'default':
        data['style']['background-color'] = bcolor
    # 发射数据
    el = e.push(Widgets.Text(data))
    print(Widgets.Text(data))
    # 操作ADOM
    if wait and not e.lock.lock_passed():
        e.lock.lock()
        e.lock.wait_for_unlock()
    return el
