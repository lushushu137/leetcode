var twoSum = function (numbers, target) {
  let right = numbers.length - 1;
  for (let i = 0; i < numbers.length; ) {
    if (numbers[i] + numbers[right] > target) {
      right--;
    } else if (numbers[i] + numbers[right] == target) {
      return [i + 1, right + 1];
    } else {
      i++;
    }
  }
};
console.log(twoSum([2, 7, 11, 15], 9));
