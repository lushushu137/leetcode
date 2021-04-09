// 慢！
// var findMin = function(nums) {
//     let minNum = nums[0];
//     for (let i = 0; i < nums.length; i++) {
//         let before = i - 1 < 0 ? nums[nums.length - 1] : nums[i-1];
//         let current = nums[i];
//         let next = i + 1 >= nums.length ? nums[0] : nums[i+1]
//         console.log(before, current, next)
//         if (before > current && current < next) {
//             minNum = current
//         }
//     }
//     return minNum
// };


var findMin = function(nums) {
    for (let i = 0; i< nums.length; i++) {
        let current = nums[i];
        let next = nums[i+1];
        if (next < current){
            return next
        }
    }
    return nums[0]
};


console.log(findMin([2,3,4,5,1]))
console.log(findMin([4,5,6,7,0,1,2]))
console.log(findMin([11,13,15,17]))
console.log(findMin([1]))
console.log(findMin([2, 1]))