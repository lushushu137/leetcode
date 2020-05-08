def climbStairs(n: int) -> int:
    s1 = 1
    s2 = 2
    s = 0
    for i in range(n):
        if i == 0:
            s = s1
        elif i == 1:
            s = s2
        else:
            print(i, s1, s2)
            s1, s2 = s2, s1 + s2
            s = s2
    return s


print(climbStairs(3))