def longestPalindrome(s):
    res = ''
    newS = '_'.join(list(s))
    for i in range(len(newS)):
        if newS[i] != '_':
            k = 0
        else:
            k = 1
        while i - k >= 0 and i + k < len(newS):
            if newS[i - k] == newS[i + k]:
                if len(res) <= len(newS[i - k:i + k + 1]) - k:
                    res = ''.join(
                        [j for j in newS[i - k:i + k + 1] if j != '_'])
                k += 2
            else:
                break
    return res


print(longestPalindrome(''))