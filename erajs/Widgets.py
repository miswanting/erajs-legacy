from . import Elements
from . import engine as e


class Widget:
    def __init__(self, data):
        if 'key' in data:
            self.__key = data['key']
        else:
            self.__key = e.new_hash()

    def create_element(self):
        pass

    def can_update(self, old_widget, new_widget) -> bool:
        pass


class StatelessWidget(Widget):
    def __init__(self, data):
        super().__init__(data)
        self.__data = {
            'key': e.new_hash(),
            'child': []
        }

    def create_element(self):
        return Elements.StatelessElement(self)

    def build(self, context):
        pass


class StatefulWidget(Widget):
    def __init__(self, data):
        super().__init__(data)
        self.__data = {
            'hash': e.new_hash(),
            'child': []
        }

    def create_element(self):
        return Elements.StatefulElement(self)

    def create_state(self):
        pass

    def build(self, context):
        pass


class Text(StatelessWidget):
    def __init__(self, data):
        super().__init__(data)
