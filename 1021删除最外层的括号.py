from collections import deque


def myfunc(S):
    mystack = deque()
    temp = ''
    res = ''
    for i in S:
        if i == '(':
            mystack.append(i)
        else:
            mystack.pop()
        temp += i

        if len(mystack) == 0:
            res += temp[1:-1]
            temp = ''

    return res
