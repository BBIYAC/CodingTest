/*
 오픈 채팅방(https://programmers.co.kr/learn/courses/30/lessons/42888)
 채팅방에 들어오고 나가거나, 
 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 
 모든 기록이 처리된 후,
  최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
 */

 function solution(record) {
    var answer = [];
    var users = {}
    for(var i=0; i<record.length; i++){
        var state = record[i].split(' ')[0]
        var userId = record[i].split(' ')[1]
        // userId를 이용해 nickName 추가 및 변경
        if(state == 'Enter' || state == 'Change'){
            var nickName = record[i].split(' ')[2]
            users[userId] = nickName
        }
    }
    
    // 정답 배열에 추가
    for(var i=0; i<record.length; i++){
        var state = record[i].split(' ')[0]
        var userId = record[i].split(' ')[1]   
        if(state == 'Enter'){
            answer.push(users[userId]+'님이 들어왔습니다.')
        }else if(state == 'Leave'){
            answer.push(users[userId]+'님이 나갔습니다.')
        }
    }
    return answer;
}