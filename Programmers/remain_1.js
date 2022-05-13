/* 나머지가 1이 되는 수 찾기 */
function solution(n) {
    var answer = 1e9;
    for(var i=0; i<n; i++){
        if(n%i == 1){
            answer = Math.min(answer, i);
        }
    }
    return answer;
}

// best answer
function solution(n) {
    for(var i=0; i<n; i++){
        if(n%i == 1){
            return i
        }
    }
}