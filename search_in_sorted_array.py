from typing import List

def search(nums: List[int], target: int) -> int:
    def find_pivot(nums: List[int], low: int, high: int) -> int:
        if low >= high:
            if low + 1 < len(nums):
                return -1 if nums[low + 1] > nums[low] else low
            elif low - 1 > 0:
                return -1 if nums[low - 1] < nums[low] else low
            return -1
        mid = (low + high) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        left = find_pivot(nums, low, mid - 1)
        if left != -1:
            return left
        return find_pivot(nums, mid + 1, high)
    
    def binary_search(nums: List[int], target: int) -> int:
        low, mid, high = 0, len(nums) // 2, len(nums) - 1
        while low <= high:
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
        return -1

    pivot_idx = find_pivot(nums, 0, len(nums) - 1)
    if pivot_idx == -1:
        return binary_search(nums, target)

    pivot = nums[pivot_idx]
    if nums[0] <= target <= pivot:
        return pivot_idx if nums[pivot_idx] == target else binary_search(nums[:pivot_idx], target)
    res = binary_search(nums[pivot_idx + 1:], target)
    if res > -1:
        return pivot_idx + 1 + binary_search(nums[pivot_idx + 1:], target)
    return res