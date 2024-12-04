def max_profit(prices: List[int]) -> int:
    maxp, minv = 0, prices[0]
    for p in prices[1:]:
        minv = min(minv, p)
        maxp = max(maxp, p - minv)
    return maxp