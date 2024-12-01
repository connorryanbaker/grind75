from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    counts = Counter(ransom_note)
    for c in magazine:
        if c in counts:
            counts[c] -= 1
    return all({ counts[c] <= 0 for c in counts })
