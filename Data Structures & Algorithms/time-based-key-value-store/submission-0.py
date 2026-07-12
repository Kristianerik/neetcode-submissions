from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.mood = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mood[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mood:
            return ""
        l = 0
        r = len(self.mood[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if self.mood[key][mid][0] == timestamp:
                return self.mood[key][mid][1]
            elif self.mood[key][mid][0] < timestamp:
                res = self.mood[key][mid][1]
                l = mid + 1
            elif self.mood[key][mid][0] > timestamp:
                r = mid - 1
        
        return res

