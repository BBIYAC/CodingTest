/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
  // Complete the function
  let distinct_nums = Array.from(new Set(nums));
  distinct_nums.sort((a, b) => b - a);
  return distinct_nums[1];
}