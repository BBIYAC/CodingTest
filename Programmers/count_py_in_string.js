/* 문자열 내 p와 y의 개수 */
function solution(s){
    var countP = 0;
    var countY = 0;
    
    for(var c of s.toUpperCase()){
        if(c === 'P'){
            countP++;
        }else if(c === 'Y'){
            countY++;
        }
    }
    
    return countP === countY? true: false;
}