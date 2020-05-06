from collections import deque

print(int(6 / (-132)))
exit()


def myfunc(token):
    mystack = deque()
    for i in token:
        print(list(mystack), i)
        if i == '+':
            mystack.append(mystack.pop() + mystack.pop())
        elif i == '-':
            late = mystack.pop()
            early = mystack.pop()
            mystack.append(early - late)

        elif i == '*':
            mystack.append(mystack.pop() * mystack.pop())

        elif i == '/':
            late = mystack.pop()
            early = mystack.pop()
            mystack.append(early // late)

        else:
            mystack.append(int(i))

    return mystack[0]


print(
    myfunc(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
