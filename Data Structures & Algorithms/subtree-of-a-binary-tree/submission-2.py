# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if root and not subRoot: return False
        if subRoot and not root: return False
        
        def sameTree(n1, n2):
            if not n1 and not n2: return True
            if n1 and not n2: return False
            if n2 and not n1: return False
            
            return n1.val == n2.val and sameTree(n1.right,    n2.right) and sameTree(n1.left, n2.left)

        return sameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        

        

        
        