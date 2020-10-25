"""Consistent Hash CacheNode class"""


class CacheNode:
    """CacheNode, record cache node info and send cache method"""
    def __init__(self, ip):
        self._ip = ip

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value: str):
        self._ip = value

    def send(self, request : str):
        """Send to data to cache, currently do nothing"""
        pass
