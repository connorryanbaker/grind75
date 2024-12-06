from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    res = []
    curr = intervals.pop(0)
    while intervals:
        ni = intervals[0]
        if overlap(curr, ni):
            curr = _merge(curr, ni)
            intervals.pop(0)
        else:
            res.append(curr)
            if intervals:
                curr = intervals.pop(0)
    return res + [curr]

def overlap(i1: List[int], i2: List[int]) -> bool:
    s1, e1 = i1
    s2, e2 = i2
    return s1 <= s2 <= e1 or s2 <= e1 <= e2 or s2 <= s1 <= e2 or s1 <= e2 <= e1

def _merge(i1: List[int], i2: List[int]) -> List[int]:
    return [ min(i1[0], i2[0]), max(i1[1], i2[1]) ]

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))