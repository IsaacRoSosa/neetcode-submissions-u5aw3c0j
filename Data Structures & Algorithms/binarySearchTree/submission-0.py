class TreeNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None 

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)
        if not self.root:
            self.root = newNode
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left == None:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right == None:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1
    
    def getMinNode(self, curr) -> TreeNode:
        while curr and curr.left:
            curr= curr.left
        return curr

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right 
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    #Remove the node with key, return new root of tree
    def removeHelper(self, curr, key) -> Optional[TreeNode]:
        if curr == None:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            # 1 or 0 children
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
            #2 children
                minNode = self.getMinNode(curr.right)
                curr.val = minNode.val
                curr.key = minNode.key
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root,result)
        return result
        
    def inorderTraversal(self,root,result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
