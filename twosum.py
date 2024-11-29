from typing import List

def twosum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, n in enumerate(nums):
        if n in lookup:
            return [lookup[n], i]
        lookup[target - n] = i
    return [-1, -1]
