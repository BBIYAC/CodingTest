/* 타겟 넘버 */

function dfs(numbers, idx, target, num){
    var answer = 0;
    if(idx == numbers.length){
        if(num == target) return 1 
        else return 0 
    }
    answer += dfs(numbers, idx+1, target, num+numbers[idx]);
    answer += dfs(numbers, idx+1, target, num-numbers[idx]);
    return answer;
}

function solution(numbers, target){
    return dfs(numbers, 0, target, 0);
}