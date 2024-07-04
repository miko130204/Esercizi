import unittest

class Node:
    pos = 0
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next
        self.pos = Node.pos
        Node.pos += 1

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val: int):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def get_node(self, index: int):
        if index == 0:
            return self.head
        
        current = self.head
        while current and current.next:
            current = current.next
            if current.pos == index:
                return current
        return None

def has_cycle(head: Node):
    if head is None:
        return False

    prev = head
    current = head.next

    if current is None:
        return False
    
    if current.pos <= prev.pos:
        return True
    
    while current and current.next:
        prev = current
        current = current.next
        if current.pos <= prev.pos:
            return True
    
    return False

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        Node.pos = 0

    def test_append_single_node(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.head.val, 1)
        self.assertIsNone(ll.head.next)

    def test_append_multiple_nodes(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        current = ll.head
        for i in range(5):
            self.assertEqual(current.val, i)
            current = current.next

    def test_get_node_by_index(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        node = ll.get_node(3)
        self.assertEqual(node.val, 3)
        self.assertEqual(node.pos, 3)

    def test_get_node_out_of_range(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        node = ll.get_node(10)
        self.assertIsNone(node)

    def test_has_cycle_in_empty_list(self):
        ll = LinkedList()
        self.assertFalse(has_cycle(ll.head))

    def test_has_cycle_in_single_node_list(self):
        ll = LinkedList()
        ll.append(1)
        self.assertFalse(has_cycle(ll.head))

    def test_has_cycle_single_node_self_loop(self):
        ll = LinkedList()
        ll.append(1)
        ll.head.next = ll.head
        self.assertTrue(has_cycle(ll.head))

    def test_has_cycle_in_multiple_nodes_no_cycle(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        self.assertFalse(has_cycle(ll.head))

    def test_has_cycle_in_multiple_nodes_with_cycle(self):
        ll = LinkedList()
        for i in range(5):
            ll.append(i)
        node1 = ll.get_node(1)
        node4 = ll.get_node(4)
        node4.next = node1
        self.assertTrue(has_cycle(ll.head))

    def test_has_cycle_long_list(self):
        ll = LinkedList()
        for i in range(100):
            ll.append(i)
        self.assertFalse(has_cycle(ll.head))

if __name__ == '__main__':
    unittest.main()