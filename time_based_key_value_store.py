from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][timestamp] = value
            self.store[key]["members"].append(timestamp)
        else:
            self.store[key] = {}
            self.store[key][timestamp] = value
            self.store[key]["members"] = [timestamp]

        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                idx = bisect_left(self.store[key]["members"], timestamp)
                ts = self.store[key]["members"][idx-1]
                return "" if idx == 0 else self.store[key][ts]
        return ""
