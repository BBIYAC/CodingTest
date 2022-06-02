/* 가장 작은 수 제거하기 */
function solution(arr) {
    var array = arr.filter(n => n > Math.min(...arr));
    return array.length > 0? array: [-1];
}