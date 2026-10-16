class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a dictionary to hold the strings
        string_count = {}
        for word in strs:
            let_freq = [0] * 26
            for let in word:
                let_freq[ord(let) - ord('a')] += 1
            if tuple(let_freq) in string_count:
                string_count[tuple(let_freq)].append(word)
            else:
                string_count[tuple(let_freq)] = [word]
        return list(string_count.values()) 
        