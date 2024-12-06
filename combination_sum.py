from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    table = [ [] for i in range(target + 1) ]

    for c in candidates:
        for subamt in range(len(table)):
            if subamt < c:
                continue
            if subamt == c:
                table[subamt].append([c])
            if c < subamt:
                subcombos = table[subamt - c]
                newsubs = []
                for s in subcombos:
                    newsubs.append(s + [c])
                table[subamt] += newsubs
        
    return table[-1]