from Singleton import Singleton


@Singleton
class Printer:
    def __init__(self, name: str = 'hp101', ip: str = '192.168.0.3'):
        self._name = name
        self.ip = ip

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value


if __name__ == '__main__':
    printer_one = Printer.instance()
    printer_one.name = 'Canon'
    printer_two = Printer.instance()
    print(f'id(printer_one) = {id(printer_one)}')
    print(f'id(printer_two) = {id(printer_two)}')
    print(printer_two.name)