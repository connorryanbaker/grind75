def can_partition(nums: List[int]) -> bool:
    if sum(nums) % 2:
        return False

    target = sum(nums) / 2
    table = [True] + [False] * target

    for n in nums:
        for j in range(target, n - 1, -1):
            table[j] = table[j] or table[j - n]
    return table[target]
