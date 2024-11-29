from typing import List

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    og_value = image[sr][sc]
    dfs(image, sr, sc, og_value, color, set())
    return image

def dfs(image: List[List[int]], r: int, c: int, target: int, update: int, lookup: set) -> None:
    if not on_board(image, r, c):
        return
    if (r, c) in lookup:
        return
    if image[r][c] != target:
        return
    image[r][c] = update
    lookup.add((r, c))
    dfs(image, r - 1, c, target, update, lookup)
    dfs(image, r + 1, c, target, update, lookup)
    dfs(image, r, c - 1, target, update, lookup)
    dfs(image, r, c + 1, target, update, lookup)

def on_board(image: List[List[int]], r: int, c: int) -> bool:
    if not image:
        return False
    if r < 0 or c < 0:
        return False
    if r >= len(image) or c >= len(image[0]):
        return False
    return True
    