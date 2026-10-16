class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # map list of frequent characters -> [word]
        # iterate through strs
        for word in strs:
            # create list of 26 chars and populate
            freq = [0] * 26
            for let in word:
                freq[ord('a') - ord(let)] += 1

        # append to correct hashmap entry
            res[tuple(freq)].append(word)

        # return values of hashmap at a lit
        return list(res.values())

