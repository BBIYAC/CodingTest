/*
모의고사에서 수포자 가장 높은 점수
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
 */

function solution(answers) {
    let array = []
    let score = [0, 0, 0];
    const person1 = [1,2,3,4,5];
    const person2 = [2,1,2,3,2,4,2,5];
    const person3 = [3,3,1,1,2,2,4,4,5,5];
    
    // 채점
    answers.forEach((answer, idx, arr)=>{
        if(answer === person1[idx % 5]){ score[0]++ };
        if(answer === person2[idx % 8]){ score[1]++ };
        if(answer === person3[idx % 10]){ score[2]++ };
    });
    
    // 가장 높은 점수 받은 사람 정답 배열에 추가
    let maxValue = Math.max(...score);
    if(score[0] === maxValue){ array.push(1) };
    if(score[1] === maxValue){ array.push(2) };
    if(score[2] === maxValue){ array.push(3) };
    
    return array.sort();
}