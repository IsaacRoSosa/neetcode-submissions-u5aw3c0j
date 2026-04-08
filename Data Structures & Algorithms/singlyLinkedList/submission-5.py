class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1
        
    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.next = self.head.next
        self.head.next = newHead
        #if the list was empty update the tail
        if not newHead.next:
            self.tail = newHead
        

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        self.tail.next = newTail
        self.tail = newTail
        
    def remove(self, index: int) -> bool:
        curr = self.head
        count = 0
        while count < index and curr:
            curr = curr.next
            count += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
