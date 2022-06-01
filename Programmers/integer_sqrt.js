/* 정수 제곱근 판별 */
function solution(n) {
    if(Number.isInteger(Math.sqrt(n))) return (Math.sqrt(n)+1)**2;
    else return -1;
}