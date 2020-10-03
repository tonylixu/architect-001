from Component import Component


class LeafComponent(Component):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def print(self):
        print(f'I am {self.get_name()}')
