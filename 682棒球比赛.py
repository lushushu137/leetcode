from collections import deque


def baseball(ops):
    roundPoint = deque()
    helper = deque()
    total = 0
    for i in ops:
        if i not in "CD+":
            roundPoint.append(int(i))
            total += int(i)
        elif i == 'C':
            total -= roundPoint[-1]
            roundPoint.pop()
        elif i == '+':
            helper.append(roundPoint.pop())
            k = helper[-1] + roundPoint[-1]
            total += k
            roundPoint.append(helper.pop())
            roundPoint.append(k)

        elif i == 'D':
            roundPoint.append(roundPoint[-1] * 2)
            total += roundPoint[-1]

    return total
