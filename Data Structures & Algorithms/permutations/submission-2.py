class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        print(perms)
        res = []
        for p in perms:
            for i in range(len(p)+1):
                p_cpy = p.copy()
                p_cpy.insert(i, nums[0])
                res.append(p_cpy)

        return res

                
            

        