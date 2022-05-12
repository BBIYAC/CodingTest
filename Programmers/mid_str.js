/* 가운데 글자 가져오기 */
function solution(s) {
    var answer = '';
    var idx = parseInt(s.length/2);
    if(s.length%2 == 0){
        answer = s.slice(idx-1, idx+1);
    }else{
        answer = s[idx];
    }
    return answer;
}