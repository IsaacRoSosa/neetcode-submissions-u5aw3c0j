# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        i = 1
        prev, curr = None, head
        #nos movemos hasta encontrar donde tenemos que llegar
        while i < left:
            prev = curr
            curr = curr.next
            i += 1
        #Limitamos la area donde hacemos el reverse
        bef, newCur, newR = None, curr, curr
        while i >= left and i <= right:
            tmp = newCur.next
            newCur.next = bef
            bef = newCur
            newCur = tmp
            i += 1
        newR.next = newCur
        if prev:
            prev.next = bef
            return head
        else:
            return bef