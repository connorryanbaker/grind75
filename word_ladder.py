from collections import defaultdict
from typing import List

def single_character_word_distance(a: str, b: str) -> bool:
    total = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            total += 1
    return total == 1

def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    target_idx = None
    if end_word not in word_list:
        return 0
    else:
        target_idx = word_list.index(end_word)

    paths = defaultdict(set)
    for i in range(len(word_list)):
        w1 = word_list[i]
        if single_character_word_distance(begin_word, w1):
            paths[-1].add(i)
            paths[i].add(-1)
        for j in range(i + 1, len(word_list)):
            w2 = word_list[j]
            if single_character_word_distance(w1, w2):
                paths[i].add(j)
                paths[j].add(i)
        
    found = False
    q = [{-1}]
    words = 0
    while q:
        words += 1
        next_level = set()
        curr = q.pop(0)
        if target_idx in curr:
            found = True
            break
        for word in curr:
            next_level = next_level.union(paths[word])
            del paths[word]
        if len(next_level) > 0:
            q.append(next_level)
    return words if found else 0

print(ladder_length("leet", "code", ["lest","leet","lose","code","lode","robe","lost"]))