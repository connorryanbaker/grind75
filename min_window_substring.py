from collections import Counter
def min_window(s: str, t: str) -> str:
    if len(Counter(t) - Counter(s)):
        return ''

    tcounts = Counter(t)
    i, j = 0, 1
    res = s
    scounts = Counter(s[i:j])
    while j < len(s):
        while not scounts >= tcounts and j < len(s):
            scounts[s[j]] += 1
            j += 1
        if scounts >= tcounts:
            if len(s[i:j]) < len(res):
                res = s[i:j]
        while i < j and scounts >= tcounts:
            if len(s[i:j]) < len(res):
                res = s[i:j]
            scounts[s[i]] -= 1
            i += 1
        while i < len(s) and s[i] not in tcounts:
            scounts[s[i]] -= 1
            i += 1
    return res

print(min_window("cabwefgewcwaefgcf", "cae"))