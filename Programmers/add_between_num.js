/* 두 정수 사이의 합 */
function solution(a, b) {
    var answer = 0;
    for(var num=(a<b? a: b); num<=(a<b? b: a); num++){
        answer += num;
    }
    return answer;
}