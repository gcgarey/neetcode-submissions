class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if the t string is empty, just return ""
        if t == "":
            return ""
        
        # initialize the dictionaries
        countT = {}
        window = {}

        # Populate the dictionary for t frequency
        for i in t:
            countT[i] = countT.get(i, 0) + 1
        
        # define what you have and what you need
        have = 0
        need = len(countT)

        # define your results (length and actual) and left pointer
        res = [-1, -1]
        reslen = float("infinity")
        l = 0

        # traverse with right pointer
        for r in range(len(s)):
            # define current character in s we're looking at
            curr = s[r]
            # populate window with the frequency of that character
            window[curr] = window.get(curr, 0) + 1
            # if current char is in t's dict and both dictionary's match, increment have
            if curr in countT and window[curr] == countT[curr]:
                have += 1
            # while we have what we need
            while have == need: 
                # if our current window is less than reslen, update our result variables
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                # before we make the window smaller, we need to decrease the frequency of our window dict
                window[s[l]] -= 1
                # if the left char in s is in t dict and we have less than we need for that char, decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # move the sliding window
                l += 1
                
        # At the end of the result, l, r is the result
        l, r = res
        # if reslen is less than what we initially set, return that string, else return ""
        if reslen != float("infinity"):
            return s[l: r + 1]
        else:
            return ""

    

        