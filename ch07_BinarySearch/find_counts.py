'''
정렬된 배열에서 특정 수의 개수 구하기
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있을 때, 이 수열에서 x가 등장하는 횟수 계산
단, 값이 x인 원소가 하나도 없다면 -1 출력

# 입력 예시 1
7 2
1 1 2 2 2 2 3

# 출력 예시 1
4

# 입력 예시 2
7 4
1 1 2 2 2 2 3

# 출력 예시 2
-1
'''

def solution():
    answer = 0
    n, x = map(int, input('>> ').split())
    array = list(map(int, input('>> ').split()))
    for num in array:
        if num == x:
            answer += 1
    if answer == 0:
        answer = -1 
    return answer

print(solution())


