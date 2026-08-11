# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        def dfs(root, total):
            if not root:
                return False 
            total += root.val
            #leaf
            if not root.left and not root.right:
                if total == targetSum:
                    return True
                else: return False
            if dfs(root.left,total):
                return True
            if dfs(root.right,total):
                return True
            total -= root.val
            
            return False
        return dfs(root,total)
            
        