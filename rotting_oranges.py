from typing import List

def oranges_rotting(grid: List[List[int]]) -> int:
    def any_rotten_neighbors(grid: List[List[int]], row: int, col: int) -> bool:
        res = []
        if row > 0:
            res.append(grid[row - 1][col])
        if row < len(grid) - 1:
            res.append(grid[row + 1][col])
        if col > 0:
            res.append(grid[row][col - 1])
        if col < len(grid[row]) - 1:
            res.append(grid[row][col + 1])
        return any([ el == 2 for el in res ])

    curr = grid
    next_gen = [ row.copy() for row in curr ]
    generations = 0
    made_swaps = True
    while made_swaps:
        made_swaps = False
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if curr[r][c] == 1 and any_rotten_neighbors(curr, r, c):
                    next_gen[r][c] = 2
                    made_swaps = True
        if made_swaps:
            generations += 1
            curr = next_gen
            next_gen = [ row.copy() for row in curr ]
    if any([ el == 1 for row in curr for el in row ]):
        return -1
    return generations
