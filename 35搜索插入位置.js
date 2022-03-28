var searchInsert = function (nums, target) {
  let left = 0;
  let right = nums.length;
  while (left < right) {
    let middle = Math.floor((left + right) / 2);
    if (nums[middle] >= target) {
      right = middle;
    } else {
      left = middle + 1;
    }
  }
  return left;
};
console.log(searchInsert([1, 3, 5, 6], 5));
