class AbstractDOM:
    """
    ## DOM操作
    ### 节点查找
    ### 节点创建
    ### 节点修改
    ### 节点关系
    """

    def __init__(self):
        self.__data = {}

    # 节点查找
    def get_root(self):  # 返回根节点。
        pass

    def get_element_by_id(self, id):  # 按ID查找元素，返回一个。
        pass

    def get_element_by_class_name(self, class_name):  # 按类名查找元素，返回列表。
        pass

    def get_element_by_widget_type(self, widget_type):  # 按控件类型查找元素，返回列表。
        pass


class Element:
    def __init__(self):
        self.__data = {}

    # 节点创建
    def append_child(self, node):
        pass

    def insert_before(self, new_node, ref_node):
        pass

    def remove_child(self, node):
        pass

    def replace_child(self, new_node, old_node):
        pass

    def set_attribute(self, name, value):
        pass

    def get_attribute(self, name):
        pass

    def has_attribute(self, name):
        pass

    def get_last_child(self):
        pass
