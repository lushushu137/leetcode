def maxSubArray(nums) -> int:
    dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = nums[i]
    max_num = nums[0]
    for i in range(len(nums)):
        for j in range(1, i):
            if dp[i][j] == None:
                dp[i][j] = dp[i][j - 1] + nums[j]
                max_num = max(max_num, dp[i][j])
                print(dp)
    return max_num


print(maxSubArray([-2, 1, -3, 4]))
