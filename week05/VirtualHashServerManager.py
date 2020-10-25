"""Class VirtualHashServerManager, maintain list of cache node"""
# Import system libs
import bisect
import random
# Import local libs
import HashServerBase


class VirtualHashServerManager(HashServerBase.HashServerBase):
    """Hash server manager, return the server for a given IP"""

    def __init__(self, virtual_node_number: int = 10):
        """Initialize HashServerManager class
        cache_list: Keep list of cache node ip hash
        cache_node: Hashmap for cache node, ip -> actual node
        """
        super().__init__()
        self.cache_list = []
        self.cache_node = {}
        self.virtual_node_number = virtual_node_number

    def add_server(self, node):
        """Add cache node
        :param node: Cache node, record cache server inforamtion
        """
        # Generate hash value based on nodes
        for i in range(self.virtual_node_number):
            node_hash = self.generate_hash(node.ip + '-' + str(i))
            # Insert node_hash into cache_list in sorted order
            bisect.insort(self.cache_list, node_hash)
            self.cache_node[node_hash] = node

    def delete_server(self, node):
        """Remove a given cache node from both cache_list and cache_node
        :param node: Cache node
        """
        node_hash = self.generate_hash(node.ip)
        self.cache_list.remove(node_hash)
        del self.cache_node[node_hash]

    def get_cache_node(self, source_key: str):
        """Based on the source_key, determine which cache node to cache"""
        key_hash = self.generate_hash(source_key)
        index = bisect.bisect_left(self.cache_list, key_hash) % len(self.cache_list)
        return self.cache_node[self.cache_list[index]]
