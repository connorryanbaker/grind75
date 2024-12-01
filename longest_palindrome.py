from collections import Counter

def longest_palindrome(s: str) -> int:
    counts, result, max_odd, max_odd_c = Counter(s), 0, 0, None
    for c in counts:
        if counts[c] % 2 == 0:
            result += counts[c]
        else:
            max_odd = max(max_odd, counts[c])
            if counts[c] == max_odd:
                max_odd_c = c
    
    if max_odd_c:
        result += counts[max_odd_c]
    
    for c in counts:
        if counts[c] % 2 != 0 and c != max_odd_c:
            result += counts[c] - 1
    return result
    