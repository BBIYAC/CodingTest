/* 부족한 금액 계산하기 */
function solution(price, money, count) {
    var sum = 0;
    for(var i=1; i<=count; i++){
        sum += price*i;
    }
    return sum>money? sum-money: 0;
}