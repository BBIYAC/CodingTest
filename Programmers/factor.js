/* 약수 */
function solution(n) {
    var answer = 0;
    for(let num=1; num<=n; num++){
        if(n%num == 0){
            answer += num;
        }
    }
    return answer;
}