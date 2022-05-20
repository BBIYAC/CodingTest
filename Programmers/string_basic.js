/* 문자열 다루기 기본 */
function solution(s) {
    return (+s === parseInt(s))? ((s.length === 4 || s.length === 6) && !isNaN(s)): false;
}
// + : 문자열이 순수 숫자 문자인지 확인(아니라면 NaN)
// isNaN : 문자열이 숫자인지 확인