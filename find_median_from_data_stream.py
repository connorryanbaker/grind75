from bisect import bisect_left
class MedianFinder:

    def __init__(self):
        self.nums = []


    def addNum(self, num: int) -> None:
        idx = bisect_left(self.nums, num)
        if idx == 0:
            self.nums = [num] + self.nums
        else:
            self.nums = self.nums[:idx] + [num] + self.nums[idx:]
        

    def findMedian(self) -> float:
        middle_idx = len(self.nums) // 2
        if len(self.nums) % 2:
            return self.nums[middle_idx]
        return (self.nums[middle_idx] + self.nums[middle_idx - 1]) / 2        
# TODO: try this one again w/ self balancing tree
