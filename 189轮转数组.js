var rotate = function (nums, k) {
  k = k % nums.length;
  const flip = (arr, start, end) => {
    while (start < end) {
      let temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
  };
  flip(nums, 0, nums.length - k - 1);
  flip(nums, nums.length - k, nums.length - 1);
  flip(nums, 0, nums.length - 1);
};
