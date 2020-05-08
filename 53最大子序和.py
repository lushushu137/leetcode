def maxSubArray(nums) -> int:
    hasThis = nums[0]
    notHasThis = -9999999999999999
    for i in range(1, len(nums)):
        notHasThis = max(hasThis, notHasThis)
        hasThis = max(hasThis + nums[i], nums[i])
    return max(hasThis, notHasThis)


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
