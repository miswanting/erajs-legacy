from . import NEngine
from . import Tools

e = NEngine.Engine()


def init():
    e.log.info('Initializing...')
    e.log.info('├─ Fixing Path...')
    Tools.fix_path()
    e.log.info('├─ Checking Program Integrity...')
    e.data.check_file_system()
    e.log.info('├─ Loading Engine Configuration...')
    e.data.load_config(['config/config.ini'])
    e.log.info('├─ Scanning Plugins...')
    # e.data.data['config']['plugin'].update(
    #     e.module.scan_plugin(
    #         e.data.data['config']['plugin']))
    # e.log.info('│  └─ {} Plugins Scanned!'.format(
    #     len(e.data.data['config']['plugin'])))
    e.log.info('├─ Loading Plugins...')
    # n,self.module.load_plugin(self.data.data['config']['plugin'])
    # self.log.info('│  └─ {} Plugins Loaded!'.format(
    #     self.module.load_plugin()))
    e.log.info('├─ Connecting Server...')
    e.net.connect()
    e.log.info('├─ Transfering Configuration to Server...')
    e.net.send_config()
    e.log.info('├─ Loading Data Files...')
    # 读data文件夹中的数据文件，扫描的同时要将信息发送到前端
    data = e.data.load_data(e.data.scan('data'), e.net.send)
    for each in data.keys():
        e.data.data[each] = data[each]
    e.log.info('│  └─ Data Files Loaded!')
    e.log.info('├─ Scanning Scripts...')
    e.log.info('│  └─ {} Scripts Scanned!'.format(
        e.module.scan_script()))
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
    e.log.info('├─ Transferring Loading Complete Signal...')
    e.net.send_loaded()
    e.log.info('└─ Initialize Complete!')


def std():
    pass


def data():
    pass


def save():
    pass
