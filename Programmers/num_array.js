/* 자연수 뒤집어 배열로 만들기 */
function solution(n) {
    var answer = [];
    var num = n;
    for(var i=0;i<n.toString().length; i++){
        answer.push(num%10);
        num = parseInt(num/10);
    }
    return answer;
}