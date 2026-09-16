# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        #Get length 
        n = 0
        curr = head
        while curr:
            n +=1
            stack.append(curr.val)
            curr = curr.next
        maxSum = 0

        for i in range(n//2):
            twinSum = stack[i] + stack.pop()
            maxSum = max(maxSum, twinSum)
        return maxSum
           
        