"""
中间件
"""

import time
import typing

from . import EventManager, LogManager, NEngine, Widgets

e = NEngine.Engine()

logger = LogManager.logger
dispatcher = EventManager.EventDispatcher()
event_type = EventManager.EventType


def print(level, *argF):
    pass


def config(**kw):
    logger.debug(kw)


def init():
    def change_init_status(e):
        nonlocal is_init_finished
        is_init_finished = True
        dispatcher.remove_all_listeners()

    e.init()
    is_init_finished = False
    dispatcher.add_listener(
        EventManager.EventType.ENGINE_INIT_FINISHED,
        change_init_status,
        one_time=True
    )
    dispatcher.dispatch(EventManager.EventType.ENGINE_INIT_STARTED)
    while True:
        if is_init_finished:
            break
        time.sleep(1)
        # dispatcher.show_listener_list()
    # e.data.check_file_system()
    # logger.info('├─ Loading Engine Configuration...')
    # e.data.load_config(['config/config.ini'])
    # logger.info('├─ Scanning Plugins...')
    # e.data.data['config']['plugin'].update(
    #     e.module.scan_plugin(
    #         e.data.data['config']['plugin']))
    # logger.info('│  └─ {} Plugins Scanned!'.format(
    #     len(e.data.data['config']['plugin'])))
    # logger.info('├─ Loading Plugins...')
    # n,self.module.load_plugin(self.data.data['config']['plugin'])
    # self.log.info('│  └─ {} Plugins Loaded!'.format(
    #     self.module.load_plugin()))
    # logger.info('├─ Connecting Server...')
    # e.net.connect()
    # logger.info('├─ Transfering Configuration to Server...')
    # e.net.send_config()
    # logger.info('├─ Loading Data Files...')
    # 读data文件夹中的数据文件，扫描的同时要将信息发送到前端
    # data = e.data.load_data(e.data.scan('data'), e.net.send)
    # for each in data.keys():
    #     e.data.data[each] = data[each]
    # logger.info('│  └─ Data Files Loaded!')
    # logger.info('├─ Scanning Scripts...')
    # logger.info('│  └─ {} Scripts Scanned!'.format(
    #     e.module.scan_script()))
    # self.log.info('├─ Loading Scripts...')
    # self.log.info('│  └─ {} Scripts Loaded!'.format(
    #     self.module.load_script(self.net.send)))
    # self.log.info('├─ Scanning DLCs...')
    # self.log.info('│  └─ {} DLCs Scanned!'.format(self.module.scan_dlc()))
    # self.log.info('├─ Loading DLCs...')
    # self.log.info('│  └─ {} DLCs Loaded!'.format(self.module.load_dlc()))
    # self.log.info('├─ Scanning MODs...')
    # self.log.info('│  └─ {} MODs Scanned!'.format(self.module.scan_mod()))
    # self.log.info('├─ Loading MODs...')
    # self.log.info('│  └─ {} MODs Loaded!'.format(self.module.load_mod()))
    # logger.info('├─ Transferring Loading Complete Signal...')
    # e.net.send_loaded()
    # logger.info('└─ Initialize Complete!')


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
