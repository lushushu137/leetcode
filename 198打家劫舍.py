def rob(nums):
    if nums == []:
        return 0
    for i in range(len(nums)):
        if i == 0:
            currMax = nums[0]
        elif i == 1:
            preMax = currMax
            currMax = max(nums[0], nums[1])
        else:
            notRob = currMax
            rob = nums[i] + preMax
            currMax = max(rob, notRob)
            preMax = notRob
    return currMax


print(rob([2, 7, 9, 3, 1]))
