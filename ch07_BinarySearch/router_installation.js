/*
공유기 설치
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
한 집에는 공유기 하나만 설치 가능, 가장 인접한 두 공유기 사이의 거리는 가능한 크게 설치

# 입력 예시 
5 3
1
2
8
4
9

# 출력 예시
3

# 힌트
공유기를 1, 4, 8 또는 1, 4, 9에 설치하면 가장 인접한 두 공유기 사이의 거리는 3이고, 이 거리보다 크게 공유기 3개 설치할 수 없음
*/

function solution(homes, c){
    var answer = 0
    var start = 0
    var end = 0
    var mid = 0
    var value = 0
    var count = 0
    var homes_length = homes.length
    homes.sort()
    start = homes[1] - homes[0] // 집의 좌표 중에서 가장 작은 값
    end = homes[homes_length-1] - homes[0] // 집의 좌표 중에서 가장 큰 값
    
    while(start<=end){
        mid = parseInt((start+end)/2) // mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
        console.log(mid)
        value = homes[0]
        count = 1
        // 현재의 mid 값을 이용해 공유기 설치
        for(var i=1; i<homes_length; i++){
            if(homes[i]>=value+mid){
                value = homes[i]
                count += 1
            }
            if(count>=c){ // c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
                start = mid+1
                answer = mid // 최적의 결과 저장
            }
            else{ // c개 이상의 공유기를 설치할 수 없는 경우 거리 감소
                end = mid-1
            }
        }
    }
    return answer
}

console.log(solution([1, 2, 8, 4, 9], 3))