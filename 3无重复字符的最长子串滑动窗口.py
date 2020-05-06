from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    if s == '':
        return 0
    mydeque = deque()
    temp = 1
    k = 0
    for i in range(len(s)):
        if s[i] not in mydeque:
            mydeque.append(s[i])
            k = len(mydeque)
        else:
            temp = max(k, temp)
            while s[i] in mydeque:
                mydeque.popleft()
            mydeque.append(s[i])
            k = len(mydeque)
    temp = max(k, temp)
    return temp


print(lengthOfLongestSubstring("abcabcbb"))