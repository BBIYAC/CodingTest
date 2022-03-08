'''
외벽 점검
외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가
담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값

친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1 return

# 입출력 예시 1
n: 12
weak: [1, 5, 6, 10]
dist: [1, 2, 3, 4]
Result: 2

# 입출력 예시 2
n: 12
weak: [1, 3, 4, 9, 10]
dist: [3, 5, 7]
Result: 1
'''
# 정답
from itertools import permutations

def answer_solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값
    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1    
    return answer

print(answer_solution(12, [1, 5, 6, 10], [1, 2, 3, 4])) # 2
print(answer_solution(12, [1, 3, 4, 9, 10], [3, 5, 7])) # 1