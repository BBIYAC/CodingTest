/* 나누어떨어지는 숫자 */
function solution(arr, divisor) {
    var answer = [];
    for(var num of arr){
        (num%divisor == 0) && answer.push(num);
    }
    return answer.length>0? answer.sort((a,b)=>a-b): [-1];
}