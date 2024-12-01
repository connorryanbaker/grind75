from collections import Counter

def majorityElement(nums: List[int]) -> int:
    # regular old solution
    # counts = Counter(nums)
    # return max(counts, key=counts.get)

    # moore's voting algoriithm
    m, c = nums[0], 1
    for n in nums[1:]:
        if c == 0:
            m, c = n, 1
        elif n == m:
            c += 1
        else:
            c -= 1
    return m