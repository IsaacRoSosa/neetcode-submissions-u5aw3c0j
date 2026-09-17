# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#El lado izquierdo siempre sera mas grande
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #We arrive at the middle of the list
        #Slow is at the end of the first halve
        prev = None
        curr = slow.next
        #Reverse the second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #Separar listas
        slow.next = None
        l2 = prev
        l1 = head

        #Construir nueva lista
        dummy = ListNode(0,None)
        ans = dummy
        
        while l1 and l2:
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next
        if l1:
            dummy.next = l1

        return None
        