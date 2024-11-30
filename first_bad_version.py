# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def first_bad_version(n: int) -> int:
    left, mid, right = 1, (n // 2) + 1, n
    fbv = None
    while left <= right:
        if isBadVersion(mid):
            fbv = mid
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return fbv