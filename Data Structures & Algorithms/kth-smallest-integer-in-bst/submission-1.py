# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.temp = 0
        self.found = 0

        def dfs(node):
            if not node: return False

            left = dfs(node.left)
            if left == True : return True
    
            self.temp += 1
            if self.temp == self.k:
                self.found = node.val
                return True

            right = dfs(node.right)
            
            return False

        dfs(root)
        return self.found
        