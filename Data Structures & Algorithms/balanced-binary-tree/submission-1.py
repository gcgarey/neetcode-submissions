# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def dfs(node):
            if not node:
                return 0
            rheight = dfs(node.right)
            lheight = dfs(node.left)
            if abs(rheight - lheight) > 1:
                self.balanced = False
            return 1 + max(rheight, lheight)

        dfs(root)
        return self.balanced



        