from collections import defaultdict
from typing import List

def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if not edges:
        return [0]
    if len(edges) == 1:
        return edges[0]

    degrees = [0] * n
    lookup = defaultdict(set)
    for e in edges:
        a, b = e
        lookup[a].add(b)
        lookup[b].add(a)
        degrees[a] += 1
        degrees[b] += 1
    
    q = []
    q.append([ i for i in range(n) if degrees[i] == 1 ])
    
    while q:
        level = q.pop(0)
        next_level = []
        for node in level:
            degrees[node] = 0
            neighbors = lookup[node]
            for n in neighbors:
                degrees[n] -= 1
                lookup[n].remove(node)
                if degrees[n] == 1:
                    next_level.append(n)
            del lookup[node]
        if next_level:
            q.append(next_level)
        else:
            return level

print(find_min_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))