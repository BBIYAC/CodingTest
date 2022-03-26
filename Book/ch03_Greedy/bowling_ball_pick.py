'''
볼링공 고르기
N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수

# 입력 조건
1. 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분
2. 각 볼링공의 무게 K가 공백으로 구분

# 출력 조건
두 사람이 볼링공 고르는 경우의 수 출력

# 입력 예시 1
5 3
1 3 2 3 2

# 출력 예시 1
8

# 입력 예시 2
8 5
1 5 4 3 2 4 5 2

# 출력 예시 2
25
'''

def solution():
    answer = 0
    # 볼링공의 개수 n, 공의 최대 무게 m
    n, m = map(int, input('>> ').split())
    # 각 볼링공의 무게 k
    k = sorted(list(map(int, input('>> ').split())))
    for i in range(1, n):
        # 두 개의 볼링공 고르는 경우
        answer += i
        # 같은 무게인 경우 제외
        if k[i] == k[i-1]:
            answer -= 1
    # 서로 다른 무게의 볼링공을 고르는 경우
    return answer

print(solution())


# 중복 무게를 리스트에 담는 방법
def answer_solution():
    answer = 0
    n, m = map(int, input('>> ').split())
    data = list(map(int, input('>> ').split()))

    # 1부터 10까지의 무게를 담을 수 있는 리스트
    array = [0] * 11
    for x in data:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        array[x] += 1

    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m+1):
        # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        n -= array[i]
        # B가 선택하는 경우의 수와 곱하기
        answer += array[i]*n
    return answer

print(answer_solution())