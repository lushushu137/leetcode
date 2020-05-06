def isHappy(n: int) -> bool:
    found = False
    memo = []
    theNewN = newN(n)
    while not found:
        if theNewN == 1:
            return True
        else:
            if sorted(str(theNewN)) in memo:
                return False
            else:
                memo.append(sorted(str(theNewN)))
                theNewN = newN(theNewN)


def newN(n):
    res = 0
    while n > 0:
        res += (n % 10)**2
        n = n // 10
    return res


print(isHappy(18))