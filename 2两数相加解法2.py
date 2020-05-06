def class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    res = ListNode(0)
    currRes = res
    carry = 0
    flag = 0
    while l1 and l2:
        p = l1.val + l2.val + carry
        if flag == 0:
            currRes.val = p%10
            carry = p//10
            flag = 1
        else:
            currRes.next = ListNode(p%10)
            currRes = currRes.next
            carry = p //10

        l1 = l1.next
        l2 = l2.next
    while l1:
        p = l1.val+ carry
        currRes.next = ListNode(p % 10)
        currRes = currRes.next
        carry = p//10
        l1 = l1.next
    while l2:
        p = l2.val+ carry
        currRes.next = ListNode(p % 10)
        currRes = currRes.next
        carry = p//10
        l2 = l2.next
    if carry == 1:
        currRes.next = ListNode(1)
    return res

   