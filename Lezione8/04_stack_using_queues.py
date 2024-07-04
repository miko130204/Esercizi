import unittest

class Queue:
    def __init__(self) -> None:
        self.queue_list = []

    def push(self, x: int):
        self.queue_list.append(x)
    
    def top(self):
        return self.queue_list[0]
    
    def pop(self):
        return self.queue_list.pop(0)
    
    def empty(self):
        return len(self.queue_list) == 0

class MyStack:
    def __init__(self) -> None:
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x : int):
        self.queue1.push(x)

    def pop(self):
        x = -1
        while not self.queue1.empty():
            x = self.queue1.pop()
            if not self.queue1.empty():
                self.queue2.push(x)

        while not self.queue2.empty():
            y = self.queue2.pop()
            self.queue1.push(y)

        return x
    
    def top(self):
        while not self.queue1.empty():
            x = self.queue1.pop()
            self.queue2.push(x)

        while not self.queue2.empty():
            y = self.queue2.pop()
            self.queue1.push(y)

        return x
    
    def empty(self):
        return self.queue1.empty()

class TestQueueAndStack(unittest.TestCase):

    def test_queue_push(self):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.queue_list, [1, 2])

    def test_queue_pop(self):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)

    def test_queue_top(self):
        q = Queue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.top(), 1)

    def test_queue_empty(self):
        q = Queue()
        self.assertTrue(q.empty())
        q.push(1)
        self.assertFalse(q.empty())
        q.pop()
        self.assertTrue(q.empty())

    def test_stack_push(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertFalse(s.empty())
        self.assertEqual(s.queue1.queue_list, [1, 2])

    def test_stack_pop(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_stack_top(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertFalse(s.empty())
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.top(), 1)

    def test_stack_empty(self):
        s = MyStack()
        self.assertTrue(s.empty())
        s.push(1)
        self.assertFalse(s.empty())
        s.pop()
        self.assertTrue(s.empty())

    def test_stack_push_pop_sequence(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        s.push(4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_stack_multiple_operations(self):
        s = MyStack()
        s.push(1)
        self.assertEqual(s.top(), 1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.top(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

if __name__ == '__main__':
    unittest.main()