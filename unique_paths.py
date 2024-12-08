def unique_paths(m: int, n: int) -> int:
    def dfs(r, c, memo):
        if (r,c) in memo:
            return memo[(r,c)]
        if r < 0 or m <= r or c < 0 or n <= c:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        right_paths = dfs(r, c + 1, memo)
        down_paths = dfs(r + 1, c, memo)
        memo[(r,c)] = right_paths + down_paths
        return memo[(r,c)]
    return dfs(0, 0, {})