// 太慢啦！！！
// var findMin = function(nums) {
//     let noRepeat = nums.reduce((cur, next) => {
//         if (next === cur) {
//             return [...cur];
//         }
//         return [...cur, next];
//     }, [nums[0]]);
//     for (let i = 0; i< noRepeat.length; i++) {
//         let current = noRepeat[i];
//         let next = noRepeat[i+1];
//         if (next < current){
//             return next
//         }
//     }
//     return noRepeat[0]
// };


var findMin = function(nums) {
    let left = 0;
    let right = 1;
    while(left <= nums.length - 1 && left <= nums.length - 1){
        let current = nums[left];
        let next = nums[right];
        if (next < current){
            return next
        } else if (next === current) {
           right++;
        } else {
            left++;
            right++
        }
    }
    return nums[0]
};


console.log(findMin([2,3,4,5,1]))
console.log(findMin([4,5,6,7,0,1,2]))
console.log(findMin([3,3,1]))
console.log(findMin([3, 5, 1]))