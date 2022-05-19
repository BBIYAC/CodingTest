/* 문자열 내림차순 정렬 */
function solution(s) {
    var arr = [];
    for(var char of s){
        arr.push(char);
    }
    arr.sort((a,b)=>{
        if(a<b) return 1;
        if(a>b) return -1;
        if(a===b) return 0;})
    return arr.join('');
}

// best answer
function solution(s) {
    var answer = s.split('').sort().reverse().join('');
    return answer;
}