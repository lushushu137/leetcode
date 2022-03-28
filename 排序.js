var sortArray = function (nums) {
  if (nums.length <= 1) {
    return nums;
  }
  if (nums.length == 2) {
    if (nums[0] == nums[1]) {
      return nums;
    }
  }
  let axis = nums[parseInt(Math.random(0, 1) * nums.length)];
  let left = [];
  let right = [];
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > axis) {
      right.push(nums[i]);
    } else {
      left.push(nums[i]);
    }
  }
  //   console.log("aixs:", axis);
  //   console.log("left:", left);
  //   console.log("right:", right);

  return [...sortArray(left), ...sortArray(right)];
};

console.log(
  sortArray([
    -7087, 12694, -19352, -7660, 12052, -11316, -352, 18321, 15, 19967, 6331,
  ])
);
