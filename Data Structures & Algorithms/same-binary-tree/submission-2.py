# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p and q : return False
        if not q and p: return False

        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
            






        if not p and not q:
            return True

        if not p and q : return False
        if not q and p: return False

        r = self.isSameTree(p.right, q.right)
        l = self.isSameTree(p.left, q.left)

        print(f"{p.val}, {q.val}")
        #print(f"{r}, {l}")

        if p != q:
            return False

        return True

        



        

        