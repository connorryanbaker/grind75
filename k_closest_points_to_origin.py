from math import sqrt

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key=self.distance_to_origin)[:k]

def distance_to_origin(point: List[int]) -> int:
    x = point[0] * -1
    y = point[1] * -1
    return sqrt(x ** 2 + y ** 2)