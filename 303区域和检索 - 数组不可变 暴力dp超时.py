class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        leng = len(self.nums)
        dp = [[None for _ in range(leng)] for _ in range(leng)]
        for k in range(leng):
            dp[k][k] = self.nums[k]
        for start in range(leng):
            for end in range(start, leng):
                if dp[start][end] == None:
                    dp[start][end] = dp[start][end - 1] + self.nums[end]
        return dp[i][j]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(2, 5))
