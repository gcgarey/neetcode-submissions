class ListNode:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key --> Node
        self.right, self.left = ListNode(0,0), ListNode(0,0)

        self.left.next, self.right.prev = self.right, self.left

    def delete(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self, Node):
        prev, nxt = self.right.prev, self.right
        prev.next = Node
        nxt.prev = Node
        Node.next, Node.prev = nxt, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        