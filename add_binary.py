def add(a: int, b: int, carry: int) -> (int, int):
    total = a + b + carry
    if total == 3:
        return (1, 1)
    elif total == 2:
        return (0, 1)
    elif total == 1:
        return (1, 0)
    return (0, 0)
    
def add_binary(a: str, b: str) -> str:
    result = []
    carry = 0
    a, b = list(a), list(b)
    while a and b:
        x, y = a.pop(), b.pop()
        total, carry = add(int(x), int(y), carry)
        result.append(total)
    if a:
        while a:
            x, y = a.pop(), 0
            total, carry = add(int(x), int(y), carry)
            result.append(total)
    elif b:
        while b:
            x, y = b.pop(), 0
            total, carry = add(int(x), int(y), carry)
            result.append(total)

    if carry:
        result.append(carry)

    return "".join([ str(x) for x in result ][::-1])