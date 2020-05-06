class MyQueue:
    def __init__(self):
        self.items = []
        self.helper = []

    def push(self, x: int) -> None:
        return self.items.append(x)

    def pop(self) -> int:
        if self.helper != []:
            return self.helper.pop()
        else:
            while self.items != []:
                self.helper.append(self.items.pop())
        return self.helper.pop()

    def peek(self) -> int:
        if self.helper != []:
            return self.helper[-1]
        else:
            while self.items != []:
                self.helper.append(self.items.pop())
        return self.helper[-1]

    def empty(self) -> bool:
        if self.items == [] and self.helper == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()