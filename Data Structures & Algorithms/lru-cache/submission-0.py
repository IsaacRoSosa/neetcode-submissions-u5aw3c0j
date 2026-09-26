class ListNode:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.pairs = {}
        self.size = capacity
        self.LRU = ListNode(0,0)
        self.MRU = ListNode(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        
    def get(self, key: int) -> int:
        if key not in self.pairs: return -1
        else: 
            cur = self.pairs[key]
            ans = cur.val
            self.remove(cur)
            self.insert(cur)
            return ans
        
    def put(self, key: int, value: int) -> None:
        newNode = ListNode(key,value)
        if key in self.pairs:
            self.remove(self.pairs[key])
        self.insert(newNode)
        self.pairs[key] = newNode
        if len(self.pairs) > self.size:
            remove = self.LRU.next
            self.pairs.pop(remove.key)
            self.remove(remove)

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: ListNode):
        prev_node = self.MRU.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.MRU
        self.MRU.prev = node

       
        
