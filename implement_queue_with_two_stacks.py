class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
        
    def pop(self) -> int:
        if self.empty():
            return None

        while self.input:
            self.output.append(self.input.pop())
        
        v = self.output.pop()

        while self.output:
            self.input.append(self.output.pop())
        return v

    def peek(self) -> int:
        if self.empty():
            return None

        return self.input[0]
        
    def empty(self) -> bool:
        return len(self.input) == 