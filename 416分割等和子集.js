nums = [1, 5, 11, 5];

var canPartition = function (nums) {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
  }

  if (sum % 2 != 0) {
    return false;
  }

  let target = sum / 2;

  let dp = [];

  for (i = 0; i < nums.length + 1; i++) {
    let row = [];
    row = new Array(target + 1).fill(false);
    row[0] = true;
    dp.push(row);
  }

  for (i = 1; i < nums.length + 1; i++) {
    for (j = 0; j < target + 1; j++) {
      dp[i][j] = dp[i - 1][j] || nums[i - 1] == j || dp[i - 1][j - nums[i - 1]];
    }
  }

  return !!dp[nums.length][target];
};

console.log(canPartition(nums));
