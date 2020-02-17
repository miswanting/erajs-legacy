from . import LockManager


class UIManager(LockManager.LockManager):
    """
    
    """

    def __init__(self):
        super().__init__()
        self.__page_stack = []

    def goto(self, func, *arg, **kw):
        self.debug('GOTO: Append [{}] to [{}] & run'.format(
            func.__name__, self._show_gui_list()))
        self.__page_stack.append((func, arg, kw))  # append_gui
        func(*arg, **kw)

    def back(self, num=1, *arg, **kw):
        for i in range(num):s
            self.debug('BACK: Pop [{}] from [{}]'.format(
                self.__page_stack[-1][0].__name__, self._show_gui_list()))
            self.__page_stack.pop()
        self.debug('BACK: & run last')
        self.__page_stack[-1][0](*self.__page_stack[-1][1], **
                                 self.__page_stack[-1][2])  # repeat

    def repeat(self, *arg, **kw):
        self.debug('REPEAT: Run [{}] in [{}]'.format(
            self.__page_stack[-1][0].__name__, self._show_gui_list()))
        self.__page_stack[-1][0](*self.__page_stack[-1]
                                 [1], **self.__page_stack[-1][2])

    def append_gui(self, func, *arg, **kw):
        self.debug('APPEND: Append [{}] to [{}]'.format(
            func.__name__, self._show_gui_list()))
        self.__page_stack.append((func, arg, kw))

    def clear_gui(self, num=0):
        if num == 0:
            self.debug('CLEAR_ALL_GUI: Set [{}] to []'.format(
                self._show_gui_list()))
            self.__page_stack.clear()
        else:
            for i in range(num):
                self.debug('CLEAR_LAST_GUI: Pop [{}] from [{}]'.format(
                    self.__page_stack[-1][0].__name__, self._show_gui_list()))
                self.__page_stack.pop()

    def get_gui_list(self):
        gui_list = []
        for each in self.__page_stack:
            gui_list.append(each[0].__name__)
        return gui_list
