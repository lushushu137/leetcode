var sortedSquares = function (nums) {
  let res = [];
  let stack = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
      stack.push(nums[i] * nums[i]);
    } else {
      if (stack.length == 0) {
        res.push(nums[i] * nums[i]);
        continue;
      } else {
        let a = stack.pop();
        let b = nums[i] * nums[i];
        if (a >= b) {
          res.push(b);
          stack.push(a);
        } else {
          res.push(a);
          i--;
        }
      }
    }
  }
  while (stack.length > 0) {
    res.push(stack.pop());
  }
  return res;
};
