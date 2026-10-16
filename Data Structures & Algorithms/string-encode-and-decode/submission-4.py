class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for word in strs:
            newString += str(len(word)) + "#" + word
        return newString

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        res = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
            j = i
        return res 
        

