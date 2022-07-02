/*
 약수의 개수와 덧셈(https://programmers.co.kr/learn/courses/30/lessons/77884)
 두 정수 left와 right가 매개변수로 주어집니다. 
 left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
 */

 // 약수의 개수 구하기
function count_num(num){
    var count = 0
    for(var i=1; i<=num; i++){
        // 나머지가 0이면 카운트
        if(num%i === 0) count++;
    }
    return count
}

function solution(left, right) {
    var answer = 0;
    for(var num=left; num<=right; num++){
        // 약수의 개수가 짝수면 +
        if(count_num(num)%2 === 0){
            answer += num
        }else{ // 약수의 개수가 홀수면 -
            answer -= num
        }
    }
    return answer;
}

// 파이썬 버전
/*
# 약수의 개수
def count_num(num):
    count = 0
    for n in range(1, num+1):
        if num%n == 0:
            count += 1
    return count

# 약수의 개수가 짝수인지 홀수인지
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        answer = answer+num if count_num(num)%2 == 0 else answer-num
    return answer
*/