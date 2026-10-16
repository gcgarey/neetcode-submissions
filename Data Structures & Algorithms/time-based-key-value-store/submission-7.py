class TimeMap:

    def __init__(self):
        self.m = {} # key : [[time, value]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.m:
            self.m[key].append([timestamp, value])
        else:
            self.m[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        search = self.m[key]
        l, r = 0, len(search) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if search[m][0] == timestamp:
                return search[m][-1]

            elif search[m][0] < timestamp:
                res = search[m][-1]
                l = m + 1
            else:
                r = m - 1
        return res
        
