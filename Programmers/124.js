/* 124 나라 */
function solution(n) {
    var answer = '';
    var nums = [4, 1, 2];
    while(n){
        answer = nums[n%3] + answer;
        n = (n%3==0)? n/3 - 1 : Math.floor(n/3);
    }
    return answer;
    // 2번째 solution
    // return n === 0? '': solution(parseInt((n-1)/3)) + [1, 2, 4][(n-1)%3];
}