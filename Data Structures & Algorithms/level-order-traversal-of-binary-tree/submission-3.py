# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root:
            queue = deque([root])
        else:
            return res

        while queue:
            l = len(queue)
            level = []
            for i in range(l):
                temp = queue.popleft()
                level.append(temp.val)

                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            res.append(level)
        
        return res

            


