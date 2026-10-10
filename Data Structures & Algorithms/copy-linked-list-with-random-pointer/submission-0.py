"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Crear copia 
        nodesMap = {None:None}
        cur = head
        while cur:
            copyNode = Node(cur.val)
            nodesMap[cur] = copyNode
            cur = cur.next 
        #Conectar valores
        cur = head
        while cur:
            copy = nodesMap[cur]
            copy.next = nodesMap[cur.next]
            copy.random = nodesMap[cur.random]
            cur = cur.next
        
        return nodesMap[head]

        