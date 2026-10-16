class TimeMap:

    def __init__(self):
        # map key --> [[time, value]]
        self.stamp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stamp[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        search = self.stamp[key]
        l, r = 0, len(search) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if search[mid][0] <= timestamp:
                res = search[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


        
