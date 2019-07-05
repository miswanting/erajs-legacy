import os
import sys
import csv
import configparser
import zipfile
import json


import yaml

from . import LogManager
# import LogManager


class DataManager:
    data = {}
    pool = []

    def __init__(self):
        self.log = LogManager.LogManager()

    def self_check(self):
        self.data = {
            "config": {
                "plugin": {},
                "dlc": {},
                "mod": {},
            },
            "class": {},
            "api": {},
            "tmp": {},
            "entity": {},
            "db": {},  # 可保存的数据
            "act": {},
            "kojo": {}
        }
        check_folder_list = [
            'config',
            'dlc',
            'logic',
            'mod',
            'data',
            'save',
            'script'
        ]
        check_file_list = [
            'config/config.ini'
        ]
        for each in check_folder_list:
            if not os.path.isdir(each):
                self.log.warn(
                    'Folder {} is not Exist. Creating...'.format(each))
                os.mkdir(each)
        for each in check_file_list:
            if not os.path.isfile(each):
                self.log.warn('File {} is not Exist. Creating...'.format(each))
                open(each, 'w')

    def load_config(self, config_path):
        config = self.load_data(config_path)
        for each in config['config.config'].keys():
            self.data['config'][each] = config['config.config'][each]

    def scan(self, path_to_folder):
        fileList = []
        for root, dirs, files in os.walk(path_to_folder):
            for each in files:
                fileList.append(root + '\\' + each)
        return fileList

    def save_to(self, save_num, save_name=''):
        self.save_file(self.data['db'],
                       'save/{}.{}.zip'.format(save_num, save_name))

    def load_from(self, save_num):
        save_file_path_list = self.scan('save')
        for each in save_file_path_list:
            if each.split('\\')[-1].split('.')[0] == str(save_num):
                self.data['db'] = self.load_file(each)

    def add(self, item):
        item['hash'] = new_hash()
        self.pool.append(item)
        return item['hash']

    def get(self, pattern):
        # 参考GraphQL的部分实现原理
        def match(item, pattern):
            found = True
            for each_key in pattern.keys():
                if not each_key in item.keys():
                    found = False
                    break
            if found:
                for each_key in pattern.keys():
                    if isinstance(pattern[each_key], dict):
                        if not match(item[each_key], pattern[each_key]):
                            found = False
                            break
                    elif not pattern[each_key] == item[each_key]:
                        found = False
                        break
                if found:
                    return True
            return False

        candidate_item = []
        for each in self.pool:
            if match(each, pattern):
                candidate_item.append(each)
        return candidate_item

    def path2dot(self, path):
        """将路径转换为点路径"""
        path = path.replace('/', '\\')
        dot = '.'.join('.'.join(path.split('.')[0:-1]).split('\\'))
        ext = path.split('.')[-1]
        return dot, ext

    def dot2path(self, dot, ext):
        """将点路径转换为路径"""
        path = '.'.join(['\\'.join(dot.split('.')), ext])
        return path

    def load_data(self, files, send_func=None):
        data = {}
        for each in files:
            key = self.path2dot(each)[0]
            # 载入文件
            self.log.info('│  ├─ Loading [{}]...'.format(each))
            if not send_func == None:
                bag = {
                    'type': 'load_text',
                    'value': 'Data: [ {} ]...'.format(key),
                    'from': 'b',
                    'to': 'r'
                }
                send_func(bag)
            data[key] = self.load_file(each)
        return data

    def save_data_to_file(self, dot_path, ext='yaml'):
        """将一个data文件夹中加载的数据重新保存回去"""
        data = self.data[dot_path]
        path_to_file = self.dot2path(dot_path, ext)
        self.save_file(data, path_to_file)

    def load_file(self, path_to_file):
        """从文件加载数据，并返回"""
        path_to_file = path_to_file.replace('/', '\\')
        ext = path_to_file.split('\\')[-1].split('.')[-1]
        data = None
        # time_start = time.time()
        if ext in ['cfg', 'config', 'ini', 'inf']:
            config = configparser.ConfigParser()
            config.read(path_to_file)
            d = dict(config._sections)
            for k in d:
                d[k] = dict(d[k])
            data = d
        elif ext == 'csv':
            with open(path_to_file, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                new_list = []
                for row in reader:
                    new_list.append(row)
            data = new_list
        elif ext == 'json':
            with open(path_to_file, 'r', encoding='utf-8') as f:
                data = json.loads(''.join(f.readlines()))
        elif ext == 'yaml':
            with open(path_to_file, 'r', encoding='utf-8') as f:
                data = yaml.load(''.join(f.readlines()))
        elif ext == 'zip':
            with zipfile.ZipFile(path_to_file) as z:
                data = {}
                for file_name in z.namelist():
                    with z.open(file_name) as f:
                        data['.'.join(file_name.split('.')[0:-1])
                             ] = json.loads(f.read())
        elif ext == 'txt':
            data = []
            with open(path_to_file, 'r') as f:
                for line in f.readlines():
                    data.append(line[:-1])
        elif ext == 'kjml':
            data = []
            with open(path_to_file, 'r') as f:
                for line in f.readlines():
                    data.append(line[:-1])
        # time_stop = time.time()
        # print('加载{}文件用时：{}ms'.format(path_to_file,
        #                              int((time_stop-time_start)*1000)))
        return data

    def save_file(self, data, path_to_file):
        """保存数据到某文件"""
        path_to_file = path_to_file.replace('/', '\\')
        ext = path_to_file.split('\\')[-1].split('.')[-1]
        time_start = time.time()
        if ext in ['cfg', 'config', 'ini', 'inf']:
            config = configparser.ConfigParser()
            config.read_dict(data)
            with open(path_to_file, 'w')as f:
                config.write(f)
        elif ext == 'csv':
            with open(path_to_file, 'w', newline='', encoding='utf-8') as f:
                reader = csv.writer(f)
                reader.writerows(data)
        elif ext == 'json':
            with open(path_to_file, 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
        elif ext == 'yaml':
            with open(path_to_file, 'w', encoding='utf-8') as f:
                f.write(yaml.dump(data, allow_unicode=True,
                                  default_flow_style=False))
        elif ext == 'zip':
            with zipfile.ZipFile(path_to_file, 'w', zipfile.ZIP_LZMA) as z:
                for key in data:
                    z.writestr('{}.json'.format(key), json.dumps(
                        data[key], ensure_ascii=False))
        elif ext == 'txt':
            with open(path_to_file, 'w') as f:
                for line in data:
                    f.write('{}\n'.format(line))
        time_stop = time.time()
        # print('保存{}文件用时：{}ms'.format(path_to_file,
        #                              int((time_stop-time_start)*1000)))