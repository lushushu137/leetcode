def removeDuplicates(self, S: str) -> str:
    mystack = deque()
    for i in S:
        if len(mystack) == 0:
            mystack.append(i)
        else:
            if mystack[-1] == i:
                mystack.pop()
            else:
                mystack.append(i)
    return ''.join(list(mystack))