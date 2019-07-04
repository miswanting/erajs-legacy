import threading

from . import LogManager
# import LogManager


class EventManager:
    _listener_list: list = []

    def __init__(self):
        self.log = LogManager.LogManager()
        pass

    def add_listener(self, type, listener, hash='', removable=True):
        new_listener = {
            'type': type,
            'listener': listener,
            'hash': hash,
            'removable': removable,
        }
        self._listener_list.append(new_listener)

    def remove_listener(self, type, listener=None, hash=''):
        for i, each in enumerate(self._listener_list):
            if each['type'] == type and each['listener'].__name__ == listener.__name__ and each['hash'] == hash:
                self._listener_list.pop(i)
                break

    def remove_all_listeners(self):
        new_listener_list = []
        for each in self._listener_list:
            if not each['removable']:
                new_listener_list.append(each)
        self._listener_list = new_listener_list

    def has_listener(self, type):
        found = False
        for each in self._listener_list:
            if each['type'] == type:
                found = True
        return found

    def dispatch_event(self, type, target='', value={}):
        event = {
            'type': type,
            'target': target,
            'value': value,
        }
        for each in self._listener_list:
            if event['type'] == each['type']:
                t = threading.Thread(
                    target=each['listener'],
                    args=(event, ),
                    kwargs={}
                )
                t.start()
