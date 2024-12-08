def max_area(height: List[int]) -> int:
    i, j = 0, len(height) - 1

    maxa = 0
    while i < j:
        maxa = max(maxa, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxa
