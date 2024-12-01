from collections import Counter
def contains_duplicate(nums: List[int]) -> bool:
    counts = Counter(nums)
    return any([ counts[c] > 1 for c in counts ])
        