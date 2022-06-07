/* 휴대폰 번호 가리기 */
function solution(phone_number) {
    var answer = '';
    for(var i=0; i<phone_number.length-4; i++){
        answer += '*';
    }
    return answer+phone_number.slice(-4);
}