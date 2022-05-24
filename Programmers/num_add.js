/* 자릿수 더하기 */
function solution(n){
    var answer = 0;
    for(var num of n.toString()){
        answer += parseInt(num);
    }
    return answer;
}