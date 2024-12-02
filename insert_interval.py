from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]
    
    overlapping_interval_idx = None
    for idx, i in enumerate(intervals):
        if self.overlaps(i, newInterval):
            overlapping_interval_idx = idx
            break
    if overlapping_interval_idx is not None:
        merged = self.merge(intervals[overlapping_interval_idx], newInterval)
        next_idx = overlapping_interval_idx + 1
        while next_idx < len(intervals) and self.overlaps(intervals[next_idx], merged):
            merged = self.merge(intervals[next_idx], merged)
            next_idx += 1
        return intervals[:overlapping_interval_idx] + [merged] + intervals[next_idx:]
    else:
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        else:
            prev_interval_idx = None
            for i in range(len(intervals) - 1):
                if intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i+1][0]:
                    prev_interval_idx = i
                    break
            assert prev_interval_idx != None
            return intervals[:prev_interval_idx + 1] +[newInterval] + intervals[prev_interval_idx + 1:]

def overlaps(i1: List[int], i2: List[int]) -> bool:
    return (i1[0] <= i2[0] <= i1[1]) or (i1[0] <= i2[1] <= i1[1]) or (i2[0] <= i1[0] <= i2[1]) or (i2[0] <= i1[0] <= i2[1])

def merge(i1: List[int], i2: List[int]) -> List[int]:
    return [min(i1[0], i2[0]), max(i1[1], i2[1])]

print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert([[3,5], [6, 7]], [1, 2]))
print(insert([[1,2], [3,5]], [6, 7]))

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]