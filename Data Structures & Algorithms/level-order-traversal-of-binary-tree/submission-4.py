# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return []
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                temp = queue.popleft()
                level.append(temp.val)
                if temp.left : queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            res.append(level)
        return res
