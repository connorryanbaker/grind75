from typing import List
def letter_combinations(digits: str) -> List[str]:
    lookup = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "1": [],
        "0": []
    }
    if not digits:
        return []
    if len(digits) == 1:
        return lookup[digits[0]]
    
    res = []
    next_digits = letter_combinations(digits[1:])
    for n in next_digits:
        for d in lookup[digits[0]]:
            res.append(d + n)
    return res
