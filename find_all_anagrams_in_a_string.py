from collections import Counter
from typing import List
def find_anagrams(s: str, p: str) -> List[int]:
    counts = Counter(p)
    res = []
    for i in range(len(s) - len(p) + 1):
        sub = s[i:i+len(p)] 
        if Counter(sub) == counts:
            res.append(i)
    return res

print(find_anagrams("abab", "ab"))