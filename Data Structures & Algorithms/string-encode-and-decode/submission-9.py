class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for word in strs:
            length = str(len(word))
            newString += length + "#"
            newString += word
        print(newString)
        return newString

             

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s)-1 and s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + length + 1
     
        return res
