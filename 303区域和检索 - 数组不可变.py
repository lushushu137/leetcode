class NumArray:
    def __init__(self, nums):
        if not nums:
            return
        self.nums = nums
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]
        for end in range(1, len(nums)):
            self.dp[end] = self.dp[end - 1] + nums[end]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(i, j)
