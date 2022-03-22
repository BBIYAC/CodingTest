'''
카드 정렬하기
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한 지 구하는 프로그램

# 입력 예시
3
10
20
40

# 출력 예시
100
'''

# 정답
import heapq

def solution():
    answer = 0
    n = int(input('>> '))
    groups = []
    for _ in range(n):
        heapq.heappush(groups, int(input('>> ')))
    # 힙에 원소가 1개 남을 때까지
    while len(groups) != 1:
        # 가장 작은 2개의 카드 묶음 꺼내기
        one = heapq.heappop(groups)
        two = heapq. heappop(groups)
        # 카드 묶음 다시 합쳐서 삽입
        sum_value = one+two
        answer += sum_value
        heapq.heappush(groups, sum_value)
    return answer

print(solution())