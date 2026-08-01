# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def findMinNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        #Explore tree until we find the delete value
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #1 or 0 Children
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else: #2 Children
            #Find smallest node in right subtree
                minNode = findMinNode(root.right) 
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            return root
        return root
        
        
        
            
