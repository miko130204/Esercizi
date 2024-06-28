# 1


# 2


# 3

def is_valid_parenthesis(s: str) -> bool:
    matching_bracket = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in matching_bracket:
            top_element = stack.pop() if stack else '#'
            if matching_bracket[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


# 4

def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
        
        
# 5


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

def is_palindrome(head: Node) -> bool:
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    
    return values == values[::-1]


# 6

def longest_palindrome(s):
    from collections import Counter
    
    char_count = Counter(s)
    length = 0
    odd_found = False
    
    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True
    
    if odd_found:
        length += 1
    
    return length