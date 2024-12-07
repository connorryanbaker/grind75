def spiral_order(matrix: List[List[int]]) -> List[int]:
    n, s, e, w = 0, len(matrix), len(matrix[0]), 0
    res = []
    while n < s and w < e:
        for i in range(w, e):
            res.append(matrix[n][i])
        for i in range(n + 1, s):
            res.append(matrix[i][e - 1])
        for i in reversed(range(w, e - 1)):
            if s - 1 == n:
                break
            res.append(matrix[s - 1][i])
        for i in reversed(range(n + 1, s - 1)):
            if e - 1 == w:
                break
            res.append(matrix[i][w])
        n += 1
        s -= 1
        w += 1
        e -= 1
    return res
    