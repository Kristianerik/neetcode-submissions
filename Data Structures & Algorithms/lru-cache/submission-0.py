class Node:

    def __init__(self):
        self.prev = None
        self.next = None
        self.key = 0
        self.val = 0

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        output = self.nodes[key]
        self.remove(self.nodes[key])
        self.insert(self.nodes[key])
        return output.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])
            self.nodes.pop(key)
        
        newNode = Node()
        newNode.key, newNode.val = key, value
        self.insert(newNode)
        self.nodes[key] = newNode

        if len(self.nodes) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            self.nodes.pop(lru.key)

    def insert(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

