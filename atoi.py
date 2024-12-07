def my_atoi(s: str) -> int:
    trimmed = s.lstrip()
    if not trimmed:
        return 0

    is_positive = trimmed[0] != '-'
    if not is_positive or trimmed[0] == '+':
        trimmed = trimmed[1:]
    
    nums = []
    while trimmed and trimmed[0].isdigit():
        nums.append(int(trimmed[0]))
        trimmed = trimmed[1:]
    
    total = 0
    power = len(nums) - 1
    for n in nums:
        total += n * 10 ** power
        power -= 1
    if total >= 2 ** 31:
        return 2 ** 31 - 1 if is_positive else 2 ** 31 * -1

    return total if is_positive else total * -1
    