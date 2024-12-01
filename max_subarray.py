def max_subarray(nums: List[int]) -> int:
    max_sum = nums[0]
    running = nums[0]
    for n in nums[1:]:
        if running < 0 and running < n:
            running = n
        else:
            running += n
        max_sum = max(running, maxSum)
    return max_sum
