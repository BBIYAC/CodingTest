/*
예산 
(https://programmers.co.kr/learn/courses/30/lessons/12982)
*/
function solution(d, budget) {
    var answer = 0;
    var change = budget;
    d.sort((a,b)=>a-b);
    for(var i=0; i<d.length; i++){
        if(d[i] <= change){
            change -= d[i];
            answer++;
        }else{
            break;
        }
    }
    return answer;
}