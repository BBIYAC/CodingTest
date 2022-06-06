/* 하샤드 수 */
function solution(x) {
    var sum = 0;
    for(var num of x.toString()){
        sum += Number(num);
    }
    return x%sum == 0;
}