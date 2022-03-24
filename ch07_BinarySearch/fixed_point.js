/*
고정점 찾기
고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬
이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램, 고정점이 없다면 -1 출력

# 입력 예시 1
5
-15 -6 1 3 7

# 출력 예시 1
3

# 입력 예시 2
7
-15 -4 2 8 9 13 15

# 출력 예시 2
2

# 입력 예시 3
7
-15 -4 3 8 9 13 15

# 출력 예시 3
-1
*/

// 시간초과
function solution(n, array){
    var answer = 0
    for (const [idx, num] of array.entries()){
        if (idx == num){
            answer = num
        }
    }
    if (answer == 0){
        answer = -1
    }
    return answer
}

console.log(solution(7, [-15, -4, 3, 8, 9, 13, 15]))