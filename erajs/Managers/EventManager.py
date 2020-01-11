import threading
from typing import Callable, List


class EventManager:
    """
    # 事件管理器
    """

    def __init__(self):
        self.__listener_list: List[dict] = []

    def on(self, type: str, listener: Callable):
        new_listener = {
            'type': type,
            'listener': listener,
            'one_time': False,
        }
        self.__listener_list.append(new_listener)
    add_listener = on

    def once(self, type, listener):
        new_listener = {
            'type': type,
            'listener': listener,
            'one_time': True,
        }
        self.__listener_list.append(new_listener)

    def remove_listener(self, type, listener):
        for i, each in enumerate(self.__listener_list):
            if each['type'] == type and \
                    each['listener'].__name__ == listener.__name__:
                self.__listener_list.pop(i)
    off = remove_listener

    def remove_all_listeners(self):
        """
        removable == False的侦听器只能被remove_listener()单独移除。
        """
        self.__listener_list.clear()

    def emit(self, type, data=None):
        event = {
            'type': type,
            'data': data
        }
        i = 0
        while i < len(self.__listener_list):
            listener = self.__listener_list[i]
            if event['type'] != listener['type']:
                i += 1
                continue
            t = threading.Thread(
                target=listener['listener'],
                args=(data, ),
                kwargs={}
            )
            if listener['one_time']:
                self.__listener_list.pop(i)
                i -= 1
            t.start()
            i += 1
    dispatch = emit

    def has_listener(self, type):
        for each in self.__listener_list:
            if each['type'] == type:
                return True
        return False

    def show_listener_list(self):
        for each in self.__listener_list:
            print(each)

    def get_listener_list(self):
        return self.__listener_list
