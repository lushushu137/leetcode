var moveZeroes = function (nums) {
  let count = 0;
  let len = nums.length;
  for (let i = 0; i < len; i++) {
    if (nums[i] == undefined) {
      break;
    }
    if (nums[i] == 0) {
      nums.splice(i, 1);
      i--;
      count++;
    }
  }
  for (let i = 0; i < count; i++) {
    nums.push(0);
  }
  console.log(nums);
};
moveZeroes([0, 1, 0, 3, 12]);
