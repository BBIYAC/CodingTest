/* 스택 기능 개발 */
function solution(progresses, speeds) {
    var answer = [];
    var count = 0;
    var release_days = 0;
    for(var i=0; i<progresses.length; i++){
        if(release_days >= Math.ceil((100 - progresses[i])/speeds[i])){
            count++;
            answer.pop();
            answer.push(count);
        }else{
            release_days = Math.ceil((100 - progresses[i])/speeds[i]);
            count = 1;
            answer.push(count);
        }
    }
    return answer;
}