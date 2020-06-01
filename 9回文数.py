def isPalindrome(x):
    strx = str(x)
    left = 0
    right = len(strx) - 1
    while left <= right:
        if strx[left] == strx[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(isPalindrome(121))
