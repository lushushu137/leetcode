from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    num1 = toInt(l1)
    num2 = toInt(l2)
    num3 = num1 + num2
    l3 = toChain(num3)
    return l3


def toInt(node):
    mydeque = deque()
    while node != None:
        mydeque.append(node.val)
        node = node.next

    k = 0
    res = 0
    while mydeque:
        res += mydeque.popleft() * (10**k)
        k += 1
    return res


def toChain(num):
    numlist = deque()
    if num == 0:
        return ListNode(0)
    while num:
        numlist.append(ListNode(num % 10))
        num = num // 10

    for node in range(len(numlist) - 1):
        numlist[node].next = numlist[node + 1]
    return numlist[0]


# node = ListNode(1)
# node.next = ListNode(2)
# node.next.next = ListNode(3)
print(toChain(123).next.val)