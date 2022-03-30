/*
완주하지 못한 선수(https://programmers.co.kr/learn/courses/30/lessons/42576)
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
*/

// 내가 풀이한 답(효율성 검사 미통과)
function solution(participant, completion) {
    // 완주한 선수 인덱스 추출하여 참가자 배열에서 삭제
    completion.forEach((person)=>{
        var index = participant.indexOf(person)
        participant.splice(index, 1) // 이거 때문에 효율성 검사 오래 걸리는 듯
    })
    // 완주하지 못한 선수 출력
    var answer = participant[0]
    return answer;
}

// 정답
function solution(participant, completion) {
    participant.sort()
    completion.sort()
    for(var i=0; i<participant.length; i++){
        if(participant[i] !== completion[i]){
            return participant[i]
        }
    }
}