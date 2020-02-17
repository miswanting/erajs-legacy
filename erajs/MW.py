"""
中间件
"""

import time
import typing

from . import NEngine, Tools
e = NEngine.Engine()


# def print(level, *argF):
#     pass


def config(**kw):
    e.debug(kw)


def init():
    print()
    e.info('Era.js Engine Initializing...')
    e.info('├─ Implementing...')
    e.init()
    e.info('├─ Fixing Path...')
    Tools.fix_path()
    e.info('├─ Checking Data Integrity...')

    def on_folder_missing(e):
        e.warn('│  ├─ Folder [{}] Missing. Creating...'.format(e.value))

    def on_file_missing(e):
        e.warn('│  ├─ File [{}] Missing. Creating...'.format(e.value))
    e.on('folder_missing', on_folder_missing)
    e.on('file_missing', on_file_missing)
    e.check_file_system()
    e.off('folder_missing', on_folder_missing)
    e.off('file_missing', on_file_missing)
    e.info('│  └─ Data Integrity Checked!')
    e.info('├─ Loading Engine Config...')
    e.load_config(['config/config.ini'])
    e.info('│  └─ Engine Config Loaded!')
    e.info('├─ Scanning Plugins...')
    plugins_found = 0

    def on_plugin_found(e):
        e.info('│  ├─ Plugin [{}] Found.'.format(e.value))
        plugins_found += 1
    e.on('plugin_found', on_plugin_found)
    e.scan_plugins()
    e.off('plugin_found', on_plugin_found)
    e.info('│  └─ {} Plugins Found!'.format(plugins_found))
    e.info('├─ Loading Plugins...')
    plugins_loaded = 0

    def on_plugin_loaded(e):
        e.info('│  ├─ Plugin [{}] Loaded.'.format(e.value))
        plugins_loaded += 1
    e.on('plugin_loaded', on_plugin_loaded)
    e.load_plugins()
    e.off('plugin_loaded', on_plugin_loaded)
    e.info('│  └─ {} Plugins Loaded!'.format(plugins_loaded))
    e.info('├─ Connecting Server...')
    e.connect()
    e.info('├─ Sending Config to Server...')
    e.send_config()
    e.info('│  └─ Config to Server Sent.')
    e.info('├─ Scanning Data Files...')
    data_files_found = 0

    def on_data_file_found(e):
        e.info('│  ├─ Data File [{}] Found.'.format(e.value))
        data_files_found += 1
    e.on('data_file_found', on_data_file_found)
    e.scan_data_files()
    e.off('data_file_found', on_data_file_found)
    e.info('│  └─ {} Data Files Found!'.format(data_files_found))
    e.info('├─ Loading Data Files...')
    data_files_loaded = 0

    def on_data_file_loaded(e):
        e.info('│  ├─ Data File [{}] Loaded.'.format(e.value))
        data_files_loaded += 1
    e.on('data_file_loaded', on_data_file_loaded)
    e.load_data_files()
    e.off('data_file_loaded', on_data_file_loaded)
    e.info('│  └─ {} Data Files Loaded!'.format(data_files_loaded))
    e.info('├─ Scanning Scripts...')
    scripts_found = 0

    def on_script_found(e):
        e.info('│  ├─ Script [{}] Found.'.format(e.value))
        scripts_found += 1
    e.on('script_found', on_script_found)
    e.scan_scripts()
    e.off('script_found', on_script_found)
    e.info('│  └─ {} Scripts Found!'.format(scripts_found))
    e.info('├─ Loading Scripts...')
    scripts_loaded = 0

    def on_script_loaded(e):
        e.info('│  ├─ Script [{}] Loaded.'.format(e.value))
        scripts_loaded += 1
    e.on('script_loaded', on_script_loaded)
    e.load_scripts()
    e.off('script_loaded', on_script_loaded)
    e.info('│  └─ {} Scripts Loaded!'.format(scripts_loaded))
    e.info('├─ Scanning DLCs...')
    dlcs_found = 0

    def on_dlc_found(e):
        e.info('│  ├─ DLC [{}] Found.'.format(e.value))
        dlcs_found += 1
    e.on('dlc_found', on_dlc_found)
    e.scan_dlcs()
    e.off('dlc_found', on_dlc_found)
    e.info('│  └─ {} DLCs Found!'.format(dlcs_found))
    e.info('├─ Loading DLCs...')
    dlcs_loaded = 0

    def on_dlc_loaded(e):
        e.info('│  ├─ DLC [{}] Loaded.'.format(e.value))
        dlcs_loaded += 1
    e.on('dlc_loaded', on_dlc_loaded)
    e.load_dlcs()
    e.off('dlc_loaded', on_dlc_loaded)
    e.info('│  └─ {} DLCs Loaded!'.format(dlcs_loaded))
    e.info('├─ Scanning MODs...')
    mods_found = 0

    def on_mod_found(e):
        e.info('│  ├─ MOD [{}] Found.'.format(e.value))
        mods_found += 1
    e.on('mod_found', on_mod_found)
    e.scan_mods()
    e.off('mod_found', on_mod_found)
    e.info('│  └─ {} MODs Found!'.format(mods_found))
    e.info('├─ Loading MODs...')
    mods_loaded = 0

    def on_mod_loaded(e):
        e.info('│  ├─ MOD [{}] Loaded.'.format(e.value))
        mods_loaded += 1
    e.on('mod_loaded', on_mod_loaded)
    e.load_mods()
    e.off('mod_loaded', on_mod_loaded)
    e.info('│  └─ {} MODs Loaded!'.format(mods_loaded))
    e.info('├─ Sending Loaded Signal to Server...')
    e.send_init_finished_signal()
    e.info('│  └─ Signal to Server Sent.')
    e.info('└─ Initialize Complete!')


def std():
    pass


def data():
    pass


def cache():
    pass


def save():
    pass


def title(text):
    e.title(text)


def goto(func, *arg, **kw):
    e.goto(func, *arg, **kw)


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
    # el = e.push(Widgets.Text(data))
    # print(Widgets.Text(data))
    # 操作ADOM
    if wait and not e.lock.lock_passed():
        e.lock.lock()
        e.lock.wait_for_unlock()
    # return el
