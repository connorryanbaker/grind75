class DoublyLinkedListNode:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # update neighbor pointers
        prev = node.prev
        nextn = node.next
        if prev:
            prev.next = nextn
        if nextn and self.head != node:
            nextn.prev = prev
        # update boundary pointers
        if self.tail == node:
            self.tail = prev if len(self.cache) > 1 else node
        if self.head != node:
            self.head.prev = node
            node.prev = None
            node.next = self.head
            self.head = node
        return node.val
        

    def put(self, key: int, value: int) -> None:
        node = self.cache[key] if key in self.cache else DoublyLinkedListNode(key, value)
        if key in self.cache:
            node.val = value
        # update neighbors
        prev = node.prev
        nextn = node.next
        if prev:
            prev.next = nextn
        if nextn and node != self.head:
            nextn.prev = prev
        # update boundary pointers
        if node == self.tail and len(self.cache) > 1:
            self.tail = prev
        if len(self.cache) == 0:
            self.head = node
            self.tail = node
        elif self.head != node:
            self.head.prev = node
            node.prev = None
            node.next = self.head
        self.head = node
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            del self.cache[self.tail.key]
            self.tail = self.tail.prev