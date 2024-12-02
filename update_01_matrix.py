from typing import List, Tuple

def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    result = []
    for row in mat:
        sub = []
        for el in row:
            if el == 0:
                sub.append(0)
            else:
                sub.append(float("inf"))
        result.append(sub)
    
    made_swaps = True
    current_target = 0
    while made_swaps:
        made_swaps = False
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if result[r][c] == current_target:
                    neighbors_to_swap = neighbors_to_swap(result, current_target, r, c) 
                    if neighbors_to_swap:
                        for n in neighbors_to_swap:
                            row, col = n
                            result[row][col] = min(current_target + 1, result[row][col])
                        made_swaps = True
        current_target += 1
    return result

def neighbors_to_swap(mat: List[List[int]], target: int, row: int, col: int) -> List[Tuple[int, int]]:
    coords = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    result = []
    for coord in coords:
        r, c = coord
        if r < 0 or len(mat) <= r or c < 0 or len(mat[r]) <= c:
            continue
        if mat[r][c] <= target + 1:
            continue
        result.append(coord)
    return resul