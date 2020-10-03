from ContainerComponent import ContainerComponent


class NamedContainerComponent(ContainerComponent):
    def __init__(self, name):
        self._name = name
        self._node_list = []

    def get_name(self):
        return self._name

    def print(self):
        if len(self._node_list) == 0:
            print(f'I am {self.get_name()}')
        for c in self._node_list:
            c.print()

    def add_node(self, c):
        self._node_list.append(c)
