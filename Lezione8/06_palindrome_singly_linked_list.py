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
        self.head: Node = None

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
        while current.next:
            current = current.next
            if current.pos == index:
                return current


def get_list_length(head) -> int:
    if not head:
        return 0
    
    current = head
    counter = 1
    while current.next:
        current = current.next
        counter += 1
    return counter


def reverse_list(head: Node):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
            
        
def is_palindrome(head: Node) -> bool:
    if not head or not head.next:
        return True
    
    length = get_list_length(head)

    sep = False
    current = head
    while current and not sep:
        current = current.next
        if current.pos >= length // 2:
            tail = reverse_list(current)
            sep = True

    current_head = head
    current_tail = tail
    while current_head and current_tail:
        if current_tail.val != current_head.val:
            return False
        
        current_head = current_head.next
        current_tail = current_tail.next

    return True


class TestLinkedList(unittest.TestCase):

    def test_case_1(self):
        ll = LinkedList()
        for value in [1, 2, 3, 2, 1]:
            ll.append(value)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_2(self):
        ll = LinkedList()
        for value in [1, 2, 3, 4, 5]:
            ll.append(value)
        self.assertFalse(is_palindrome(ll.head))

    def test_case_3(self):
        ll = LinkedList()
        ll.append(1)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_4(self):
        ll = LinkedList()
        for value in [1, 1]:
            ll.append(value)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_5(self):
        ll = LinkedList()
        for value in [1, 2]:
            ll.append(value)
        self.assertFalse(is_palindrome(ll.head))

    def test_case_6(self):
        ll = LinkedList()
        self.assertTrue(is_palindrome(ll.head))

    def test_case_7(self):
        ll = LinkedList()
        for value in [1, 2, 2, 1]:
            ll.append(value)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_8(self):
        ll = LinkedList()
        for value in [1, 2, 3, 3, 2, 1]:
            ll.append(value)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_9(self):
        ll = LinkedList()
        for value in [1, 2, 3, 4, 3, 2, 1]:
            ll.append(value)
        self.assertTrue(is_palindrome(ll.head))

    def test_case_10(self):
        ll = LinkedList()
        for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            ll.append(value)
        self.assertFalse(is_palindrome(ll.head))


if __name__ == '__main__':
    unittest.main()