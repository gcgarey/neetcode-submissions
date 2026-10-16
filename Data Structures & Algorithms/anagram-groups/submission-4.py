class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # [characters by aski] : [words]

        for word in strs:
            temp = [0] * 26
            for let in word:
                idx = ord(let) - ord('a')
                temp[idx] += 1
            
            tup = tuple(temp)
            if tup in res:
                res[tup].append(word)
            else:
                res[tup] = [word]

        return list(res.values())

        