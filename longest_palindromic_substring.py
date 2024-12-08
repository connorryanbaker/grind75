def longest_palindrome(s: str) -> str:
    def expand_even(s, i):
        if i == 0:
            return s[i] 
        j = i - 1
        if s[i] != s[j]:
            return s[i]
            
        while 0 <= j and i < len(s) and s[j] == s[i]:
            i += 1
            j -= 1
        return s[j+1:i]
    def expand_odd(s, i):
        if i == 0 or i == len(s) - 1:
            return s[i]
        j = i - 1
        k = i + 1
        while 0 <= j and k < len(s) and s[j] == s[k]:
            k += 1
            j -= 1
        return s[j+1:k]
    
    if not s:
        return s
    if len(s) == 1:
        return s

    maxlen = 0
    res = None
    for i in range(len(s)):
        even = expand_even(s, i)
        if len(even) > maxlen:
            maxlen = len(even)
            res = even
        odd = expand_odd(s, i)
        if len(odd) > maxlen:
            maxlen = len(odd)
            res = odd
    return res
