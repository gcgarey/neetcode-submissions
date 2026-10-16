class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # aski[] : [words]

        for word in strs:
            temp = [0] * 26
            for ch in word:
                temp[ord('a') - ord(ch)] += 1
            temp = tuple(temp)
            res[temp].append(word)

        return list(res.values())
        