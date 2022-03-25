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

console.log(solution(7, [-15, -4, 2, 8, 9, 13, 15]))

// 정답
function binary_search(array, start, end){
    if (start > end){
        return -1;
    }
    mid = (start+end) / 2
    // 고정점을 찾은 경우 인덱스 반환
    if (array[mid] == mid){
        return mid;
    }
    // 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    else if (array[mid] > mid){
        return binary_search(array, start, mid-1);
    }
    // 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else{
        return binary_search(array, mid+1, end);
    }
}

function answer_solution(n, array){
    var answer = 0;

    // 이진탐색 수행
    var index = binary_search(array, 0, n-1);

    // 고정점이 없는 경우 -1 출력
    if (index == -1){
        answer = -1;
    }else{ // 고정점이 있는 경우 해당 인덱스 출력
        answer = index;
    }
    return answer
}


console.log(answer_solution(7, [-15, -4, 2, 8, 9, 13, 15]))