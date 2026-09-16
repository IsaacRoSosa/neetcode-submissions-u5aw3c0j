# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        coyote, correcaminos = head, head

        while correcaminos and correcaminos.next:
            coyote = coyote.next
            correcaminos = correcaminos.next.next
        return coyote