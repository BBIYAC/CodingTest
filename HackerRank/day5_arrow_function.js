/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
  return nums.map((num) => {
      if (num % 2 === 0) return num * 2;
      else return num * 3;
  })
}

function main() {
  const n = +(readLine());
  const a = readLine().split(' ').map(Number);
  
  console.log(modifyArray(a).toString().split(',').join(' '));
}