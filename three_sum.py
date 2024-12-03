def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = set()
    i = 0
    while i < len(nums):
        j, k = i + 1, len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                result.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
        i += 1
        

    return [ list(el) for el in list(result) ]