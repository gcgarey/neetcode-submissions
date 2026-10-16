class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # aski[] : [words]

        for word in strs:
            temp = [0] * 26
            for ch in word:
                temp[ord('a') - ord(ch)] += 1
            temp = tuple(temp)
            if temp in res:
                res[temp].append(word)
            else:
                res[temp] = [word]

        return list(res.values())
        