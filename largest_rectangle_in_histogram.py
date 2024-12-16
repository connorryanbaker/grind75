from typing import List

def largest_rectangle_area(heights: List[int]) -> int:
    if len(heights) == 1:
        return heights[0]
    stack = []
    ns = [-1] * len(heights)
    ps = [-1] * len(heights)
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            idx = stack.pop()
            ns[idx] = i
        if stack:
            ps[i] = stack[-1]
        stack.append(i)
    maxa = 0

    for i, h in enumerate(heights):
        ri = ns[i]
        li = ps[i]
        w = None
        if ri > -1 and li > -1:
            w = ri - li - 1
            nsw = ns[ri] - i if ns[ri] != -1 else len(heights) - i
            maxa = max(maxa, heights[ri] * nsw)
        elif ri > -1:
            # there is no previous smaller element
            w = max(ri - i - 1, 1)
            nsw = ri if ri != -1 else i + 1
            maxa = max(maxa, h * nsw)
        elif li > -1:
            # there is no next smaller element
            w = max(i - li - 1, 1)
            maxa = max(maxa, h * (len(heights) - i))
        else:
            # this is the smallest element
            w = len(heights)
        maxa = max(maxa, h * w)
    return maxa

print(largest_rectangle_area([5,4,4,6,3,2,9,5,4,8,1,0,0,4,7,2]) == 20)