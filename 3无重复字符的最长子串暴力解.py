def lengthOfLongestSubstring(s: str) -> int:
    tempmax = 1
    for left in range(len(s)):
        k = 1
        for right in range(left + 1, len(s)):
            print(s[right], s[left:right])
            if s[right] not in s[left:right]:
                k += 1
                if k > tempmax:
                    tempmax = k
            else:
                break
    return tempmax


print(lengthOfLongestSubstring("au"))
