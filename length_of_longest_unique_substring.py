def length_of_longest_substring(s: str) -> int:
    max_len = 0
    start_idx = 0
    lookup = {}

    for i, c in enumerate(s):
        if c in lookup:
            start_idx = max(start_idx, lookup[c] + 1)
            lookup[c] = i
        else:
            lookup[c] = i
        max_len = max(max_len, i + 1 - start_idx)
    return max_len
