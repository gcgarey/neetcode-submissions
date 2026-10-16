# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
          
        def dfs(node, tempmax):
            if not node: 
                return 
            if node.val >= tempmax:
                self.res += 1
                dfs(node.right, node.val)
                dfs(node.left, node.val)
            else:
                dfs(node.left, tempmax)
                dfs(node.right, tempmax)

        dfs(root, root.val)
        return self.res


        
                


        