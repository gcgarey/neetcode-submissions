# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # global variable for diameter (max(right, left) + 1)
        self.res = 0

        # helper function for dfs on current node
        def dfs(node):
            if node is None:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # update diameter for each node
            self.res = max(left_height + right_height, self.res)
            # return the max height at the current node
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.res
        
        
        

