class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        # index into the list of strings:
        for word in strs:
            # make a counts list for the 26 alphabet chars
            counts = [0] * 26
            #index into the letters to populate the list
            for char in word: 
                counts[ord(char) - ord('a')] += 1
            # add the counts list as a key and the word list as a list to result
            result[tuple(counts)].append(word)

        # return the values of the defualtdict (list of words)
        return(result.values())