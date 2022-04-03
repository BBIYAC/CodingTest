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