class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            _, curr_min = self.stack[-1]
            self.stack.append((val, min(val, curr_min)))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        v, _ = self.stack[-1]
        return v

    def getMin(self) -> int:
        if self.stack:
            _, cm = self.stack[-1]
            return cm
        return 0
