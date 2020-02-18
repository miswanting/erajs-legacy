from . import NetManager


class ProtocolManager(NetManager.NetManager):
    def __init__(self):
        super().__init__()

    def get_null_bag(self):
        bag = {
            'type': '',
            'value': '',
            'from': 'b',
            'to': 'r'
        }
        return bag

    def get_bag(self, type_name):
        bag = self.get_null_bag()
        bag['type'] = type_name
        return bag
