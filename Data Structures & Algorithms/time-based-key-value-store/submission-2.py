class TimeMap:

    def __init__(self):
        self.keydict = {}
        
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keydict:
            self.keydict[key] = []
        self.keydict[key].append([value, timestamp])
        
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.keydict.get(key, [])

        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][-1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res
        
        

        
