import os
import configparser
import sys

from . import LogManager
from . import NEngine
# import LogManager
# import NEngine


class ModuleManager:
    def __init__(self):
        self.log = LogManager.LogManager()

    def scan_plugin(self, plugin_config):
        "扫描插件的现实状况"
        config = {
            'plugin': {}
        }
        path = os.path.dirname(os.path.abspath(__file__))
        plugin_path_list = self.scan('{}/plugin'.format(path))
        # 提取插件名称
        plugin_name_list = []
        for each in plugin_path_list:
            plugin_name = '.'.join(each.replace(
                '/', '\\').split('\\')[-1].split('.')[0:-1])
            self.log.info('│  ├─ Scanning [{}]...'.format(plugin_name))
            plugin_name_list.append(plugin_name)
        # 比对配置信息
        for plugin_name in plugin_name_list:
            if not plugin_name.lower() in plugin_config:
                plugin_config[each.lower()] = 'no'
        # 同步
        return plugin_config  # TODO: 写回到文件
        # config = configparser.ConfigParser()
        # config.read_dict(e.data.data['config'])
        # with open('config/config.ini', 'w') as configfile:
        #     config.write(configfile)
        # return len(plugin_path_list)

    def scan(self, path_to_folder):
        fileList = []
        for root, dirs, files in os.walk(path_to_folder):
            for each in files:
                fileList.append(root + '\\' + each)
        return fileList

    def load_plugin(self, plugin_config):
        num_of_loaded_plugins = 0
        path = os.path.dirname(os.path.abspath(__file__))
        for each in plugin_config:
            if e.data.data['config']['plugin'][each] == 'yes':
                plugin_path_list = self.scan('{}/plugin'.format(path))
                for every in plugin_path_list:
                    module_name = '.'.join(every.replace(
                        '/', '\\').split('\\')[-1].split('.')[0:-1])
                    if module_name.lower() == each:
                        self.log.info(
                            '│  ├─ Loading [{}]...'.format(module_name))
                        # importlib.import_module('')
                        with open(every, 'r', encoding='utf8') as target:
                            sys.argv = [self]
                            exec(''.join(target.readlines()))
                        num_of_loaded_plugins += 1
        return num_of_loaded_plugins

    def scan_script(self):
        # 扫描插件文件
        script_path_list = self.scan('script')
        # 提取插件名称
        script_name_list = []
        for each in script_path_list:
            script_name = '.'.join(each.replace(
                '/', '\\').split('\\')[-1].split('.')[0:-1])
            self.log.info('│  ├─ Scanning [{}]...'.format(script_name))
            script_name_list.append(script_name)
        return len(script_path_list)

    def load_script(self, send_func=None):
        num_of_loaded_script = 0
        script_path_list = self.scan('script')
        for every in script_path_list:
            module_name = '.'.join(every.replace(
                '/', '\\').split('\\')[-1].split('.')[0:-1])
            self.log.info('│  ├─ Loading [{}]...'.format(module_name))
            if not send_func == None:
                bag = {
                    'type': 'load_text',
                    'value': 'Script: [ {} ]...'.format(module_name),
                    'from': 'b',
                    'to': 'r'
                }
                send_func(bag)
            with open(every, 'r', encoding='utf8') as target:
                sys.argv = [self]
                exec(''.join(target.readlines()))
            num_of_loaded_script += 1
        return num_of_loaded_script

    def scan_dlc(self):
        # 扫描插件文件
        dlc_path_list = self.scan('dlc')
        # 提取插件名称
        dlc_name_list = []
        for each in dlc_path_list:
            dlc_name = '.'.join(each.replace(
                '/', '\\').split('\\')[-1].split('.')[0:-1])
            self.log.info('│  ├─ Scanning [{}]...'.format(dlc_name))
            dlc_name_list.append(dlc_name)
        # 比对配置信息
        for each in dlc_name_list:
            if not each.lower() in e.data.data['config']['dlc'].keys():
                e.data.data['config']['dlc'][each.lower()] = 'no'
        # 同步
        config = configparser.ConfigParser()
        config.read_dict(e.data.data['config'])
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
        return len(dlc_path_list)

    def load_dlc(self):
        num_of_loaded_dlcs = 0
        for each in e.data.data['config']['dlc'].keys():
            if e.data.data['config']['dlc'][each] == 'yes':
                dlc_path_list = self.scan('dlc')
                for every in dlc_path_list:
                    module_name = '.'.join(every.replace(
                        '/', '\\').split('\\')[-1].split('.')[0:-1])
                    if module_name.lower() == each:
                        self.log.info(
                            '│  ├─ Loading [{}]...'.format(module_name))
                        with open(every, 'r', encoding='utf8') as target:
                            sys.argv = [self]
                            exec(''.join(target.readlines()))
                        num_of_loaded_dlcs += 1
        return num_of_loaded_dlcs

    def scan_mod(self):
        # 扫描插件文件
        mod_path_list = self.scan('mod')
        # 提取插件名称
        mod_name_list = []
        for each in mod_path_list:
            mod_name = '.'.join(each.replace(
                '/', '\\').split('\\')[-1].split('.')[0:-1])
            self.log.info('│  ├─ Scanning [{}]...'.format(mod_name))
            mod_name_list.append(mod_name)
        # 比对配置信息
        for each in mod_name_list:
            if not each.lower() in e.data.data['config']['mod'].keys():
                e.data.data['config']['mod'][each.lower()] = 'no'
        # 同步
        config = configparser.ConfigParser()
        config.read_dict(e.data.data['config'])
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)
        return len(mod_path_list)

    def load_mod(self):
        num_of_loaded_mods = 0
        for each in e.data.data['config']['mod'].keys():
            if e.data.data['config']['mod'][each] == 'yes':
                mod_path_list = self.scan('mod')
                for every in mod_path_list:
                    module_name = '.'.join(every.replace(
                        '/', '\\').split('\\')[-1].split('.')[0:-1])
                    if module_name.lower() == each:
                        self.log.info(
                            '│  ├─ Loading [{}]...'.format(module_name))
                        with open(every, 'r', encoding='utf8') as target:
                            sys.argv = [self]
                            exec(''.join(target.readlines()))
                        num_of_loaded_mods += 1
        return num_of_loaded_mods
