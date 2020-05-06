from math import sqrt
from collections import deque


def numSquares(n):
    mydeque = deque()
    for i in range(int(sqrt(n / 4)), int(sqrt(n)) + 1):
        # print(range(int(sqrt(n / 4)), int(sqrt(n))))
        if i**2 < n:
            tup = (i**2, n - i**2)
            mydeque.append(tup)
        if i**2 == n:
            return 1

    k = 1
    currSum = n
    while mydeque:

        layer = range(len(mydeque))
        for _ in layer:
            currNum = mydeque.popleft()
            currSum = currNum[1]
            for i in range(1, int(sqrt(currSum)) + 1):
                if i**2 < currSum:
                    tup = (i**2, currSum - i**2)
                    # print(currNum, tup, k)
                    mydeque.append(tup)
                if i**2 == currSum:
                    return k + 1
        k += 1


print(numSquares(17))
