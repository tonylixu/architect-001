"""Get linked list intersection node class"""
import ListNode


class NodeIntersection:
    def __init__(self):
        pass

    @staticmethod
    def get_node_intersection(head_a: ListNode, head_b: ListNode) -> ListNode:
        """Two pointers traverse two linked list

        :param head_a: Head pointer of linked list 1
        :param head_b: Head pointer of linked list 2
        :return: common node
        """
        pa, pb = head_a, head_b
        while pa != pb:
            pa = pa.next if pa else head_b
            pb = pb.next if pb else head_a
        return pa

    @staticmethod
    def create_linked_list(node_value_list):
        """Construct linked list from give list

        :param node_value_list: Python list with node values
        :return: Head node of the constructed list
        """
        temp = head = ListNode.ListNode(node_value_list[0])
        for v in node_value_list:
            node = ListNode.ListNode(v)
            temp.next = node
            temp = temp.next
        return head


def construct_two_linked_list_with_intersection(nt):
    # Construct linked list A
    # [4, 1, 8, 4, 5]
    head_a = nt.create_linked_list([4, 1, 8, 4, 5])
    temp, common_node = head_a, None
    while temp:
        if temp.val == 8:
            common_node = temp
        temp = temp.next

    # Construct linked list B
    # [5, 6, 1, 8, 4, 5]
    head_b = ListNode.ListNode(5)
    head_b.next = ListNode.ListNode(6)
    head_b.next.next = ListNode.ListNode(1)
    head_b.next.next.next = common_node

    return head_a, head_b


def main():
    nt = NodeIntersection()
    # Construct two linked list that has intersection
    head_a, head_b = construct_two_linked_list_with_intersection(nt)
    common_node = nt.get_node_intersection(head_a, head_b)
    print('Two linked list has intersection')
    print(f'     4 -> 1 \ ')
    print(f'             -> 8 -> 4 -> 5')
    print(f'5 -> 6 -> 1 /')
    print(f'Common node: {common_node.val if common_node else None}')

    # Construct two lists have no intersection
    # [1, 9, 1, 2, 4] and [3, 2, 4]
    head_a = nt.create_linked_list([1, 9, 1, 2, 4])
    head_b = ListNode.ListNode([3, 2, 4])
    common_node = nt.get_node_intersection(head_a, head_b)
    print('Two linked list has no intersection')
    print('1 -> 9 -> 1 -> 2 -> 4')
    print('3 -> 2 -> 4')
    print(f'Common node: {common_node.val if common_node else None}')


if __name__ == '__main__':
    main()
