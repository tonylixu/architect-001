"""Base class for HashServer"""
import abc
import hashlib


class HashServerBase(abc.ABC):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def add_server(self, node):
        pass

    @abc.abstractmethod
    def delete_server(self, node):
        pass

    @abc.abstractmethod
    def get_cache_node(self, source_key):
        pass

    @staticmethod
    def generate_hash(hash_str):
        md5_str = hashlib.md5(str(hash_str).encode('utf-8')).hexdigest()
        return int(md5_str, 16)