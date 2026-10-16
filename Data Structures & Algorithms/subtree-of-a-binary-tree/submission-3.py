# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # returns subRoot in the root, left, or right subtrees
        if not root and not subRoot:
            return True
        if root and not subRoot: return True
        if subRoot and not root: return False

        def sameTree(r, s):
            if not r and not s:
                return True
            if r and not s: return False
            if s and not r: return False

            return r.val == s.val and sameTree(r.right, s.right) and sameTree(r.left, s.left)

        return sameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        