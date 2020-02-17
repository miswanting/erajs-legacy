# coding:utf-8

# 自有库
from .Managers import ScriptManager


# 设计第一，架构第二，技术第三，实现第四
# 多快好省，力争上游，为开发世界一流游戏引擎而不懈奋斗!


class Engine(ScriptManager.ScriptManager):
    ENGINE_VERSION: str = '0.1.0-191029'
    PROTOCOL_VERSION: str = '0.1.0-191029'
    API_VERSION: str = '0.1.0-191029'

    def __init__(self) -> None:  # 架构初始化
        """
        初始化顺序原则：
        先基本，再高级；
        先静态，再动态；
        先抽象，再具体；
        先部分，再整体。
        Debug => Event => Data => Lock => Net => Protocol => API => Script => Engine
        └             Core              ┴        System       ┴        User        ┘
        Engine
        Script
        API
        Protocol Lock Data
        Net           Event
        Event
        Debug
        """
        super().__init__()
        print()
        self.info('Era.js Game Engine')
        self.info('Engine Version: v{}'.format(self.ENGINE_VERSION))
        self.info('Protocol Version: v{}'.format(self.PROTOCOL_VERSION))
        self.info('API Version: v{}'.format(self.API_VERSION))
        self.info('Copyright © 2018-2019 Miswanting')

    def init(self):
        pass


if __name__ == '__main__':
    e = Engine()
    e.init()
