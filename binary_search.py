def search(nums: List[int], target: int) -> int:
    left, mid, right = 0, len(nums) // 2, len(nums) - 1
    while left <= right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return -1