def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return [[]]
    
    res = []
    for i, el in enumerate(nums):
        perms_without = permute(nums[:i] + nums[i+1:])
        for perm in perms_without:
            res.append(perm +[el])
    return res
