class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for i in range(len(s1)):
            dict1[s1[i]] = dict1.get(s1[i], 0) + 1

        for j in range(len(s2)):
            dict2 = {}
            curr = 0
            for k in range(j, len(s2)):
                dict2[s2[k]] = dict2.get(s2[k], 0) + 1
                if dict1.get(s2[k], 0) < dict2.get(s2[k], 0):
                    break
                if dict1.get(s2[k], 0) == dict2[s2[k]]:
                    curr += 1
                if curr == len(dict1):
                    return True
        return False
            
        
        
            

                 
        

        