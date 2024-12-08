from typing import List, Set
def exist(board: List[List[str]], word: str) -> bool:
    def dfs(r: int, c: int, word: str, seen: Set):
        if not word:
            return True
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        if board[r][c] != word[0]:
            return False
        if (r, c) in seen:
            return False
        seen.add((r, c))
        
        if dfs(r + 1, c, word[1:], seen.copy()) or dfs(r - 1, c, word[1:], seen.copy()):
            return True
            
        if dfs(r, c + 1, word[1:], seen.copy()) or dfs(r, c - 1, word[1:], seen.copy()):
            return True
        return False
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == word[0]:
                if dfs(r, c, word, set()):
                    return True
    return False

print(exist([["a","b"],["c","d"]], "cdba"))