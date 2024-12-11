from typing import List
def trap(height: List[int]) -> int:
    maxl = [0] * len(height)
    maxr = [0] * len(height)
    for i in range(len(height)):
        if i > 0:
            maxl[i] = max(maxl[i - 1], height[i - 1])
    for i in reversed(range(len(height) - 1)):
        if i < len(height) - 1:
            maxr[i] = max(maxr[i + 1], height[i + 1])
    
    return sum([ max(min(maxl[i], maxr[i]) - height[i], 0) for i in range(len(height)) ])
print(trap([4,2,0,3,2,5]))