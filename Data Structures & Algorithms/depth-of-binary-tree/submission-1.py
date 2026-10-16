# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Find the depth of the left subtree
        lheight = self.maxDepth(root.left)

        # Find the depth of the right subtree
        rheight = self.maxDepth(root.right)

        # compare my results
        return max(lheight, rheight) + 1
        
        