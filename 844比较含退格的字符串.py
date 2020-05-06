def backspaceCompare(self, S: str, T: str) -> bool:
    from collections import deque
    stack1 = deque()
    stack2 = deque()
    for i in S:
        if i != '#':
            stack1.append(i)
        elif i == '#' and len(stack1) != 0:
            stack1.pop()
        elif i == '#' and len(stack1) == 0:
            continue
    for j in T:
        if j != '#':
            stack2.append(j)
        elif j == '#' and len(stack2) != 0:
            stack2.pop()
        elif j == '#' and len(stack2) == 0:
            continue
    if list(stack1) == list(stack2):
        return True
    else:
        return False
