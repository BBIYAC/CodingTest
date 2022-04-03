/*
체육복
전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
 */

function solution(n, lost, reserve) {
    // 체육복을 잃어버리지 않은 학생 수
    let answer = n - lost.length;
    lost.sort();
    reserve.sort();
    
    for(var lost_student of lost){
        // 체육복을 잃어버린 학생이 여벌 옷이 있는 경우
        if(reserve.includes(lost_student)) {
            reserve = reserve.filter(student=> student !== lost_student);
            answer ++;
        // 체육복을 잃어버린 학생 앞의 학생이 여벌 옷이 있는 경우
        }else if(reserve.includes(lost_student-1)){
            reserve = reserve.filter(student=> student !== lost_student-1);
            answer ++;
        // 체육복을 잃어버린 학생 뒤의 학생이 여벌 옷이 있는 경우
        }else if(reserve.includes(lost_student+1)){
            reserve = reserve.filter(student=> student !== lost_student+1);
            answer ++;
        }
    }
    return answer;
}

// 답안
function solution(n, lost, reserve) {
    let answer = 0;
    const uniform = [];
    
    // 0) 모두가 체육복을 1벌씩 가지고 있도록 설정
    for (let i = 0; i < n; i++) {
        uniform[i] = 1;
    }
    
    // 1) 체육복을 도난당한 학생의 체육복을 0개로 수정
    for (let i = 0; i < lost.length; i++) {    
        uniform[lost[i]-1] = 0;
    }
    
    // 2) 여벌의 체육복을 가져온 학생의 체육복을 +1개로 수정
    for (let i = 0; i < reserve.length; i++) {
        uniform[reserve[i]-1] += 1;
    }
    
    // 3-1) 체육복이 0개인 학생이 앞번호에서 체육복을 빌려올 수 있는 경우
    for (let i = 0; i < n; i++) {
        if (uniform[i-1] === 2 && uniform[i] === 0) {
            uniform[i-1] = 1;
            uniform[i] = 1;
    
    // 3-2) 체육복이 0개인 학생이 뒷번호에서 체육복을 빌려올 수 있는 경우
        } else if (uniform[i] === 0 && uniform[i+1] === 2) {
            uniform[i] = 1;
            uniform[i+1] = 1;
        }
    }
    
    // 결과: 체육복을 1개 이상 가지고 있게 된 학생의 수를 카운트 후, 답안 제출
    for (let i = 0; i < n; i++) {
        if (uniform[i] > 0) {
            answer++;
        }
    }
    
    return answer;
}