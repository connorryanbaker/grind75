from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[]]
    
    next_subs = subsets(nums[1:]) 
    for i in range(len(next_subs)):
        next_subs.append([nums[0]] + next_subs[i])
    return next_subs

print(subsets([1,2,3])) # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]