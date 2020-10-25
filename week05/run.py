import random
import string
import CacheNode as CacheNode
import HashServerManager as HashServerManager
import VirtualHashServerManager

# Define test range
TEST_RANGE = 1000000


def get_cache_ips():
    """Define 10 random IPs"""
    return [
        '10.11.1.1', '10.11.1.2',
        '10.11.1.3', '110.11.1.4',
        '192.168.10.1', '192.168.10.2',
        '192.168.10.3', '192.168.10.4',
        '172.14.10.15', '172.14.10.16',
        '172.14.10.17', '172.14.10.18'
    ]


def get_random_source_key(length: int = 16):
    """Generate random 16 length key"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def get_standard_deviation(cache_info):
    cache_size = len(cache_info)
    expected_num = sum(cache_info.values()) / float(cache_size)
    temp = sum([(x - expected_num)**2 for x in cache_info.values()])
    standard_deviation = (float(temp) / cache_size) ** 0.5

    return standard_deviation


if __name__ == '__main__':
    # cache_ips = get_cache_ips()
    # hash_manager = VirtualHashServerManager.VirtualHashServerManager(virtual_node_number=15)
    # for ip in cache_ips:
    #     source_key = get_random_source_key()
    #     cache_node = CacheNode.CacheNode(ip)
    #     hash_manager.add_server(cache_node)
    #     send_node = hash_manager.get_server(source_key)
    #     print(f'CacheNode: {send_node.ip}')
    # print(hash_manager.cache_list)
    # print(hash_manager.cache_node)
    cached_ips = get_cache_ips()
    simple_distribution, virtual_distribution = {}, {}
    simple_hash_server_manager, virtual_hash_server_manager = \
        HashServerManager.HashServerManager(), VirtualHashServerManager.VirtualHashServerManager()
    # Initialize all values to 0
    for ip in cached_ips:
        simple_distribution[ip] = 0
        virtual_distribution[ip] = 0

    # Create CacheNode based on IP, and add to hash server manager
    for ip in cached_ips:
        cache_node = CacheNode.CacheNode(ip)
        simple_hash_server_manager.add_server(cache_node)
        virtual_hash_server_manager.add_server(cache_node)

    #
    for _ in range(0, TEST_RANGE):
        source_key = get_random_source_key()
        simple_node = simple_hash_server_manager.get_cache_node(source_key)
        simple_distribution[simple_node.ip] += 1
        virtual_node = virtual_hash_server_manager.get_cache_node(source_key)
        virtual_distribution[virtual_node.ip] += 1

    simple_distribution_deviation = get_standard_deviation(simple_distribution)
    virtual_distribution_deviation = get_standard_deviation(virtual_distribution)
    print(simple_distribution_deviation)
    print(virtual_distribution_deviation)
