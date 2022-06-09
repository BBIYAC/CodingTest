/* x 간격이 있는 n개의 숫자 */
function solution(x, n) {
    var answer = [];
    for(var i=1; i<=n; i++){
        answer.push(i*x);
    }
    return answer;
}