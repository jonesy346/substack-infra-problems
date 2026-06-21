"""
Question:

A Redis list is a data structure that serves as the queue for the popular broker BullMQ. Write a simple Python script that implements a toy one (a Redis list is simply a linked list with string values and O(1) access at head and tail).

Answer:

We'll use a simple linked list implementation to mimic the behavior of a Redis list. The Redis list supports operations like pushing and popping elements from both ends of the list, which we will implement in our `RedisList` class.
"""

class RedisListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class RedisList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def left_push(self, value):
        """
        Push a value to the left (head) of the list.
        """
        new_node = RedisListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def right_push(self, value):
        """
        Push a value to the right (tail) of the list.
        """
        new_node = RedisListNode(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def left_pop(self):
        """
        Pop a value from the left (head) of the list.
        """
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1
        return value

    def right_pop(self):
        """
        Pop a value from the right (tail) of the list.
        """
        if not self.tail:
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1
        return value
    
redisList = RedisList()
redisList.left_push("task1")
redisList.right_push("task2")
redisList.left_push("task3")
print(redisList.left_pop())  # task3
print(redisList.right_pop())  # task2
print(redisList.left_pop())  # task1
print(redisList.left_pop())  # None

