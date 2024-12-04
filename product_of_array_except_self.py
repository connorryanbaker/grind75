from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    prefix, suffix = [], []

    running = 1
    for n in nums:
        running *= n
        prefix.append(running)
    running = 1
    for n in reversed(nums):
        running *= n
        suffix.append(running)
    suffix.reverse()
    
    result = [] 
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix[i - 1])
        else:
            result.append(prefix[i - 1] * suffix[i + 1])
    return result