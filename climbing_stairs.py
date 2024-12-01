def climb_stairs(n: int) -> int:
    steps = [0, 1, 2]
    while (n + 1) > len(steps):
        steps.append(steps[-1] + steps[-2])
    return steps[n]
            