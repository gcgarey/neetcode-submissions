# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs will take a node, left, and right
        def dfs(node, low, high):
            if not node: return True
            if low < node.val < high:
                left = dfs(node.left, low, node.val)
                right = dfs(node.right, node.val, high)
                if left == False or right == False:
                    return False
                return True
            else:
                return False
            
        
        return dfs(root, float('-inf'), float('inf'))
            