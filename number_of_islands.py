def num_islands(grid: List[List[str]]) -> int:
    def dfs(grid: List[List[str]], row: int, col: int) -> None:
        if grid[row][col] != '1':
            return
        grid[row][col] = '0'
        
        if row + 1 < len(grid):
            dfs(grid, row + 1, col)
        if row - 1 >= 0:
            dfs(grid, row - 1, col)
        if col + 1 < len(grid[row]):
            dfs(grid, row, col + 1)
        if col - 1 >= 0:
            dfs(grid, row, col - 1)
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                total += 1
                dfs(grid, i, j)
    return total