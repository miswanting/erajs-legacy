from . import engine as e


class Widget:
    def __init__(self):
        self.__key = e.new_hash()
        self.__data = {}
        self.__style = {}

    def set_state(self, data):
        pass


class Text(Widget):
    def __init__(self, data):
        super().__init__()
