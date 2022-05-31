/* 정수 내림차순으로 정렬하기 */
function solution(n) {
    var arr = [];
    for(var num of n.toString()){
        arr.push(num);
    }
    return Number(arr.sort((a,b)=>b-a).join(""));
}