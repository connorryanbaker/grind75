from collections import Counter
from typing import List
def least_interval(tasks: List[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max_count = sum([ 1 if c == max_count else 0 for c in list(counts.values())])
    with_intervals_of_n = (max_count - 1) * (n + 1) + num_max_count
    return max(len(tasks), with_intervals_of_n)
