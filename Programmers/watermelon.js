/* 수박 */
function solution(n) {
    var answer = '';
    for(var i=1; i<=n; i++){
        if(i%2 == 0) answer+="박"
        if(i%2 != 0) answer+="수"
    }
    return answer;
}