/* 콜라츠 추측 */
function solution(num) {
    var answer = 0;
    var n = num;
    while(n!=1){
        if(n%2 == 0){
            n = parseInt(n/2);
        }else{
            n = parseInt(n*3)+1;
        }
        if(answer === 500){
            return -1;
        }else{
            answer++;    
        }
    }
    return answer;
}