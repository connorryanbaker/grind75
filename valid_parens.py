def valid_parents(s: str) -> bool:
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{" 
    }
    stack = []
    for c in s:
        if c in close_to_open:
            if not len(stack) or stack.pop() != close_to_open[c]:
                return False
        else:
            stack.append(c)

    return len(stack) == 0

