from typing import List

import math
def eval_rpn(tokens: List[str]) -> int:
    lookup = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: math.ceil(x / y) if x // y < 0 else math.floor(x / y)
    }
    nums = []
    for t in tokens:
        if t not in lookup:
            nums.append(int(t))
        else:
            y, x = nums.pop(), nums.pop()
            res = lookup[t](x, y)
            nums.append(res)
    return nums[0]