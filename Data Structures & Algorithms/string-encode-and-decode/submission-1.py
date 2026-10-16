class Solution:

    def encode(self, strs: List[str]) -> str:
         # make a new string
        newString = ""
         # use a for loop to populate the newString with the list of words (prefaced with the length and # sign)
        for word in strs: 
            newString += str(len(word)) + "#" + word
         # return that result
        return newString

    def decode(self, s: str) -> List[str]:
        # create result (a list)
        result = []
        # create a pointer to keep track of where we are in the string
        i = 0
        #use a while loop to iterate through the string
        while i < len(s):
            # create another pointer equal to the first
            j = i
            # while the string at pointer2 is not #
            while s[j] != "#":
                # increment j by 1 
                j += 1
            # now we know the length is the string from i : j
            length = int(s[i:j])
            result.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
        return result

