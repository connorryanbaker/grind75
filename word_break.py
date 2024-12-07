import re
def word_break(s: str, wordDict: List[str]) -> bool:
    def helper(s: str, lookup: dict) -> bool:
        if not s:
            return True
        if s in lookup:
            return lookup[s]
        
        for word in wordDict:
            substring_idxs = [m.start() for m in re.finditer(word, s)]
            for i in substring_idxs:
                if helper(s[:i], lookup) and helper(s[i + len(word):], lookup):
                    lookup[s] = True
                    return True
        lookup[s] = False
        return False
    return helper(s, {})