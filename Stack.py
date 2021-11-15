class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value) -> None:
        self.stack.append(value)

    def pop(self) -> any:
        return self.stack.pop()

    def peek(self) -> any:
        return self.stack[len(self.stack) - 1]

    def size(self) -> int:
        return len(self.stack)
