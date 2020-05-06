class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []

    def push(self, x: int) -> None:
        print(self.items)
        if self.items == [] or x < self.top():
            print('此时的min栈1：', self.mins)
            self.mins.append(x)
            print('此时的min栈2：', self.mins)
        return self.items.append(x)

    def pop(self) -> None:
        if self.top() == self.mins[-1]:
            self.mins.pop()
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]

    def showMin(self):
        return self.mins


mystack = MinStack()
mystack.push(-2)
mystack.push(0)
mystack.push(-1)
