# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            queue = deque([root])
        else:
            return []

        while queue:
            l = len(queue)
            level = []
            for i in range(l):
                temp = queue.popleft()
                level.append(temp.val)

                if temp.left: queue.append(temp.left)
                if temp.right: queue.append(temp.right)
            print(level)
            if len(level) > 0:
                res.append(level[-1])
        return res
                
        