/* 같은 숫자는 싫어 */
function solution(arr)
{
    var answer = [arr[0]];
    for(var i=1; i<arr.length; i++){
        (arr[i-1] != arr[i]) && answer.push(arr[i]);
    }
    return answer;
}